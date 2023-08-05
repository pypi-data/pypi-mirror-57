import types
from opcode import HAVE_ARGUMENT, EXTENDED_ARG

from py_pal.metric cimport AVG_BUILTIN_FUNCTION_COMPLEXITY, CallMetric

cdef class OpcodeMetric:
    def __init__(self):
        self.hits = 0
        self.builtin_calls = 0

    cdef Py_ssize_t get_value(self, FrameType frame):
        return 1

    cdef Py_ssize_t get_function_opcodes(self, object function, object args, object kwargs):
        cdef CallMetric instance

        if isinstance(function, types.BuiltinFunctionType):
            # Statistics
            self.builtin_calls += 1
            if function in AVG_BUILTIN_FUNCTION_COMPLEXITY:
                self.hits += 1

        if function in AVG_BUILTIN_FUNCTION_COMPLEXITY:
            complexity_class = AVG_BUILTIN_FUNCTION_COMPLEXITY[function]
            instance = complexity_class(*args, **kwargs)
            return instance.value()

        return 1

cdef unpack_oparg(code):
    # Code from dis.py
    cdef int extended_arg = 0
    for i in range(0, len(code), 2):
        op = code[i]
        if op >= HAVE_ARGUMENT:
            arg = code[i + 1] | extended_arg
            extended_arg = (arg << 8) if op == EXTENDED_ARG else 0
        else:
            arg = None
        return arg

cdef class AdvancedOpcodeMetric(OpcodeMetric):
    cdef Py_ssize_t get_value(self, FrameType frame):
        if frame.f_lasti < 0:
            return 1

        code = frame.f_code.co_code
        op = code[frame.f_lasti]

        if op == 131:
            # CALL_FUNCTION
            argc = unpack_oparg(code[frame.f_lasti:])
            valuestack = <list> get_valuestack(<PyFrameObject*> frame, argc + 1)
            args = valuestack[1:]
            _callable = valuestack[0]

            return self.get_function_opcodes(_callable, args, {})

        elif op == 141:
            # CALL_FUNCTION_KW
            argc = unpack_oparg(code[frame.f_lasti:])
            valuestack = <list> get_valuestack(<PyFrameObject*> frame, argc + 2)

            _callable = valuestack.pop(0)
            kw_names = valuestack.pop()
            kwargs = {}
            for name in kw_names:
                kwargs[name] = valuestack.pop()

            return self.get_function_opcodes(_callable, valuestack, kwargs)

        return 1
