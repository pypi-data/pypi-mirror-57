"""Utilities for inline type annotations."""

from pytype import abstract
from pytype import abstract_utils
from pytype import function
from pytype import mixin
from pytype import utils
from pytype.overlays import typing_overlay

import six


class AnnotationsUtil(utils.VirtualMachineWeakrefMixin):
  """Utility class for inline type annotations."""

  # Define this error inside AnnotationsUtil so that it is exposed to
  # typing_overlay.py.
  class LateAnnotationError(Exception):
    """Used to break out of annotation evaluation if we discover a string."""

  def sub_annotations(self, node, annotations, substs, instantiate_unbound):
    """Apply type parameter substitutions to a dictionary of annotations."""
    if substs and all(substs):
      return {name: self.sub_one_annotation(node, annot, substs,
                                            instantiate_unbound)
              for name, annot in annotations.items()}
    return annotations

  def sub_one_annotation(self, node, annot, substs, instantiate_unbound=True):
    """Apply type parameter substitutions to an annotation."""
    if isinstance(annot, abstract.TypeParameter):
      def contains(subst, annot):
        return (annot.full_name in subst and subst[annot.full_name].bindings and
                not any(isinstance(v, abstract.AMBIGUOUS_OR_EMPTY)
                        for v in subst[annot.full_name].data))
      if all(contains(subst, annot) for subst in substs):
        vals = sum((subst[annot.full_name].data for subst in substs), [])
      elif instantiate_unbound:
        vals = annot.instantiate(node).data
      else:
        vals = [annot]
      return self.vm.convert.merge_classes(vals)
    elif isinstance(annot, abstract.ParameterizedClass):
      type_parameters = {
          name: self.sub_one_annotation(
              node, param, substs, instantiate_unbound)
          for name, param in annot.formal_type_parameters.items()}
      # annot may be a subtype of ParameterizedClass, such as TupleClass.
      if isinstance(annot, abstract.LiteralClass):
        # We can't create a LiteralClass because we don't have a concrete value.
        typ = abstract.ParameterizedClass
      else:
        typ = type(annot)
      return typ(annot.base_cls, type_parameters, self.vm, annot.template)
    elif isinstance(annot, abstract.Union):
      options = tuple(self.sub_one_annotation(node, o, substs,
                                              instantiate_unbound)
                      for o in annot.options)
      return type(annot)(options, self.vm)
    return annot

  def add_scope(self, annot, types, module):
    """Add scope for type parameters.

    In original type class, all type parameters that should be added a scope
    will be replaced with a new copy.

    Args:
      annot: The type class.
      types: A type name list that should be added a scope.
      module: Module name.

    Returns:
      The type with fresh type parameters that have been added the scope.
    """
    if isinstance(annot, abstract.TypeParameter):
      if annot.name in types:
        new_annot = annot.copy()
        new_annot.module = module
        return new_annot
      return annot
    elif isinstance(annot, abstract.TupleClass):
      annot.formal_type_parameters[abstract_utils.T] = self.add_scope(
          annot.formal_type_parameters[abstract_utils.T], types, module)
      return annot
    elif isinstance(annot, abstract.ParameterizedClass):
      for key, val in annot.formal_type_parameters.items():
        annot.formal_type_parameters[key] = self.add_scope(val, types, module)
      return annot
    elif isinstance(annot, abstract.Union):
      annot.options = tuple(self.add_scope(option, types, module)
                            for option in annot.options)
      return annot
    return annot

  def get_type_parameters(self, annot):
    """Get all the TypeParameter instances that appear in the annotation."""
    if isinstance(annot, abstract.TypeParameter):
      return [annot]
    elif isinstance(annot, abstract.TupleClass):
      return self.get_type_parameters(
          annot.formal_type_parameters[abstract_utils.T])
    elif isinstance(annot, abstract.ParameterizedClass):
      return sum((self.get_type_parameters(p)
                  for p in annot.formal_type_parameters.values()), [])
    elif isinstance(annot, abstract.Union):
      return sum((self.get_type_parameters(o) for o in annot.options), [])
    return []

  def convert_function_type_annotation(self, name, typ):
    visible = typ.data
    if len(visible) > 1:
      self.vm.errorlog.ambiguous_annotation(self.vm.frames, visible, name)
      return None
    else:
      return visible[0]

  def convert_function_annotations(self, node, raw_annotations):
    """Convert raw annotations to dicts of annotations and late annotations."""
    if raw_annotations:
      # {"i": int, "return": str} is stored as (int, str, ("i", "return"))
      names = abstract_utils.get_atomic_python_constant(raw_annotations[-1])
      type_list = raw_annotations[:-1]
      annotations_list = []
      for name, t in zip(names, type_list):
        name = abstract_utils.get_atomic_python_constant(name)
        t = self.convert_function_type_annotation(name, t)
        annotations_list.append((name, t))
      return self.convert_annotations_list(node, annotations_list)
    else:
      return {}, {}

  def convert_annotations_list(self, node, annotations_list):
    """Convert a (name, raw_annot) list to annotations and late annotations."""
    annotations = {}
    late_annotations = {}
    for name, t in annotations_list:
      if t is None:
        continue
      try:
        annot = self._process_one_annotation(node, t, name, self.vm.frames)
      except self.LateAnnotationError:
        late_annotations[name] = abstract.LateAnnotation(
            t, name, self.vm.simple_stack())
      else:
        if annot is not None:
          annotations[name] = annot
    return annotations, late_annotations

  def convert_class_annotations(self, node, raw_annotations):
    """Convert a name -> raw_annot dict to annotations."""
    annotations = {}
    for name, t in raw_annotations.items():
      try:
        # Don't use the parameter name, since it's often something unhelpful
        # like `0`.
        annot = self._process_one_annotation(node, t, None, self.vm.frames)
      except self.LateAnnotationError:
        # Copy the late annotation back into the dict for
        # convert_function_annotations to deal with.
        # TODO(rechen): Handle it here so that the raw annotation isn't
        # accidentally used elsewhere.
        annotations[name] = t
      else:
        annotations[name] = annot or self.vm.convert.unsolvable
    return annotations

  def eval_function_late_annotations(self, node, func, f_globals, f_locals):
    """Resolves an instance of LateAnnotation's expression."""
    for name, annot in six.iteritems(func.signature.late_annotations):
      if name == function.MULTI_ARG_ANNOTATION:
        try:
          self._eval_multi_arg_annotation(node, func, f_globals, f_locals,
                                          annot)
        except abstract_utils.EvaluationError as e:
          self.vm.errorlog.invalid_function_type_comment(
              annot.stack, annot.expr, details=e.details)
        except abstract_utils.ConversionError:
          self.vm.errorlog.invalid_function_type_comment(
              annot.stack, annot.expr, details="Must be constant.")
      else:
        resolved = self._process_one_annotation(
            node, annot.expr, annot.name, annot.stack, f_globals, f_locals)
        if resolved is not None:
          func.signature.set_annotation(name, resolved)
    func.signature.check_type_parameter_count(
        self.vm.simple_stack(func.get_first_opcode()))

  def eval_class_late_annotations(self, node, cls, f_globals, f_locals):
    """Resolves an instance of LateAnnotation's expression."""
    for name, annot in six.iteritems(cls.late_annotations):
      instance = self.init_annotation(
          node, annot.expr, annot.name, annot.stack, f_globals, f_locals)
      cls.set_annotation(name, instance)

  def init_annotation_var(self, node, name, var):
    """Instantiate a variable of an annotation, calling __init__."""
    try:
      typ = abstract_utils.get_atomic_value(var)
    except abstract_utils.ConversionError:
      error = "Type must be constant for variable annotation"
      self.vm.errorlog.invalid_annotation(self.vm.frames, None, error, name)
      return self.vm.new_unsolvable(node)
    else:
      if self.get_type_parameters(typ):
        self.vm.errorlog.not_supported_yet(
            self.vm.frames, "using type parameter in variable annotation")
        return self.vm.new_unsolvable(node)
      try:
        return self.init_annotation(node, typ, name, self.vm.frames)
      except self.LateAnnotationError:
        return abstract.LateAnnotation(typ, name, self.vm.simple_stack())

  def apply_type_comment(self, state, op, name, value):
    """If there is a type comment for the op, return its value."""
    assert op is self.vm.frame.current_opcode
    if op.code.co_filename != self.vm.filename:
      return value
    if not op.type_comment:
      return value
    comment = op.type_comment
    frame = self.vm.frame
    try:
      var = abstract_utils.eval_expr(
          self.vm, state.node, frame.f_globals, frame.f_locals, comment)
    except abstract_utils.EvaluationError as e:
      self.vm.errorlog.invalid_type_comment(
          self.vm.frames, comment, details=e.details)
      value = self.vm.new_unsolvable(state.node)
    else:
      try:
        typ = abstract_utils.get_atomic_value(var)
      except abstract_utils.ConversionError:
        self.vm.errorlog.invalid_type_comment(
            self.vm.frames, comment, details="Must be constant.")
        value = self.vm.new_unsolvable(state.node)
      else:
        if self.get_type_parameters(typ):
          self.vm.errorlog.not_supported_yet(
              self.vm.frames, "using type parameter in type comment")
        try:
          value = self.init_annotation(state.node, typ, name, self.vm.frames)
        except self.LateAnnotationError:
          value = abstract.LateAnnotation(typ, name, self.vm.simple_stack())
    return value

  def init_annotation(self, node, annot, name, stack, f_globals=None,
                      f_locals=None):
    """Instantiate the annotation, calling __init__."""
    processed = self._process_one_annotation(
        node, annot, name, stack, f_globals, f_locals)
    if processed is None:
      value = self.vm.new_unsolvable(node)
    else:
      _, value = self.vm.init_class(node, processed)
    return value

  def process_annotation_var(self, node, var, name, stack):
    new_var = self.vm.program.NewVariable()
    for b in var.bindings:
      annot = self._process_one_annotation(node, b.data, name, stack)
      if annot is None:
        return self.vm.new_unsolvable(node)
      new_var.AddBinding(annot, {b}, node)
    return new_var

  def init_from_annotations(self, node, name, annots_var):
    """Instantiate `name` from the given annotations dict, calling __init__."""
    try:
      annots = abstract_utils.get_atomic_python_constant(annots_var, dict)
    except abstract_utils.ConversionError:
      return None
    if name not in annots:
      return None
    return self.init_annotation_var(node, name, annots[name])

  def _eval_multi_arg_annotation(self, node, func, f_globals, f_locals, annot):
    """Evaluate annotation for multiple arguments (from a type comment)."""
    args = self._eval_expr_as_tuple(node, f_globals, f_locals, annot.expr)
    code = func.code
    expected = code.get_arg_count()
    names = code.co_varnames

    # This is a hack.  Specifying the type of the first arg is optional in
    # class and instance methods.  There is no way to tell at this time
    # how the function will be used, so if the first arg is self or cls we
    # make it optional.  The logic is somewhat convoluted because we don't
    # want to count the skipped argument in an error message.
    if len(args) != expected:
      if expected and names[0] in ["self", "cls"]:
        expected -= 1
        names = names[1:]

    if len(args) != expected:
      self.vm.errorlog.invalid_function_type_comment(
          annot.stack, annot.expr,
          details="Expected %d args, %d given" % (expected, len(args)))
      return
    for name, arg in zip(names, args):
      resolved = self._process_one_annotation(node, arg, name, annot.stack)
      if resolved is not None:
        func.signature.set_annotation(name, resolved)

  def _process_one_annotation(self, node, annotation, name, stack,
                              f_globals=None, f_locals=None, seen=None):
    """Change annotation / record errors where required."""

    # Check for recursive type annotations so we can emit an error message
    # rather than crashing.
    if seen is None:
      seen = set()
    if isinstance(annotation, abstract.AbstractOrConcreteValue):
      if annotation in seen:
        self.vm.errorlog.not_supported_yet(
            stack, "Recursive type annotations",
            details="In annotation '%s' on %s" % (annotation.pyval, name))
        return None
      seen = seen | {annotation}

    if isinstance(annotation, abstract.AnnotationContainer):
      annotation = annotation.base_cls

    if isinstance(annotation, typing_overlay.Union):
      self.vm.errorlog.invalid_annotation(
          stack, annotation, "Needs options", name)
      return None
    elif (name is not None and name != "return"
          and isinstance(annotation, typing_overlay.NoReturn)):
      self.vm.errorlog.invalid_annotation(
          stack, annotation, "NoReturn is not allowed", name)
      return None
    elif isinstance(annotation, abstract.Instance) and (
        annotation.cls == self.vm.convert.str_type or
        annotation.cls == self.vm.convert.unicode_type
    ):
      # String annotations : Late evaluation
      if isinstance(annotation, mixin.PythonConstant):
        if f_globals is None:
          raise self.LateAnnotationError()
        else:
          try:
            v = abstract_utils.eval_expr(
                self.vm, node, f_globals, f_locals, annotation.pyval)
          except abstract_utils.EvaluationError as e:
            self.vm.errorlog.invalid_annotation(stack, annotation, e.details)
            return None
          if len(v.data) == 1:
            return self._process_one_annotation(
                node, v.data[0], name, stack, f_globals, f_locals, seen)
      self.vm.errorlog.invalid_annotation(
          stack, annotation, "Must be constant", name)
      return None
    elif annotation.cls == self.vm.convert.none_type:
      # PEP 484 allows to write "NoneType" as "None"
      return self.vm.convert.none_type
    elif isinstance(annotation, abstract.ParameterizedClass):
      for param_name, param in annotation.formal_type_parameters.items():
        processed = self._process_one_annotation(
            node, param, name, stack, f_globals, f_locals, seen)
        if processed is None:
          return None
        elif isinstance(processed, typing_overlay.NoReturn):
          self.vm.errorlog.invalid_annotation(
              stack, param, "NoReturn is not allowed as inner type", name)
          return None
        annotation.formal_type_parameters[param_name] = processed
      return annotation
    elif isinstance(annotation, abstract.Union):
      options = []
      for option in annotation.options:
        processed = self._process_one_annotation(
            node, option, name, stack, f_globals, f_locals, seen)
        if processed is None:
          return None
        elif isinstance(processed, typing_overlay.NoReturn):
          self.vm.errorlog.invalid_annotation(
              stack, option, "NoReturn is not allowed as inner type", name)
          return None
        options.append(processed)
      annotation.options = tuple(options)
      return annotation
    elif isinstance(annotation, (mixin.Class,
                                 abstract.AMBIGUOUS_OR_EMPTY,
                                 abstract.TypeParameter,
                                 typing_overlay.NoReturn)):
      return annotation
    else:
      self.vm.errorlog.invalid_annotation(stack, annotation, "Not a type", name)
      return None

  def _eval_expr_as_tuple(self, node, f_globals, f_locals, expr):
    """Evaluate an expression as a tuple."""
    if not expr:
      return ()

    result = abstract_utils.get_atomic_value(
        abstract_utils.eval_expr(self.vm, node, f_globals, f_locals, expr))
    # If the result is a tuple, expand it.
    if (isinstance(result, mixin.PythonConstant) and
        isinstance(result.pyval, tuple)):
      return tuple(abstract_utils.get_atomic_value(x) for x in result.pyval)
    else:
      return (result,)
