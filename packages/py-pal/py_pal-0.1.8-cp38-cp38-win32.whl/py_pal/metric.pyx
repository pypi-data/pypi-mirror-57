from cpython.object cimport PyObject_GetAttr
cdef class CallMetric:
    """
        Average case complexities

        Generally, 'n' is the number of elements currently in the container.
        'k' is either the value of a parameter or the number of elements in the parameter.

        As in:  https://wiki.python.org/moin/TimeComplexity
        TODO: How should this be weighted ? C functions are faster
            The resulting value should be somewhat equivalent to counting bytecode instructions
    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    cdef public Py_ssize_t value(self):
        raise NotImplementedError("Must be implemented by subclass.")

cdef class ArgsLengthLinear(CallMetric):
    cdef public Py_ssize_t value(self):
        if PyObject_GetAttr(self.args[0], '__iter__'):
            return len(self.args[0])
        return len(self.args)

AVG_BUILTIN_FUNCTION_COMPLEXITY = {
    max.__qualname__: ArgsLengthLinear,
    sorted.__qualname__: ArgsLengthLinear,
}
