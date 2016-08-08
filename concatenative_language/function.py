class Function:
    """
    Attributes:
    built_in: boolean indicating whether a function is built in (callback) or interpreted (list of instructions)
    function: callback or list of instructions (depending on c_flag) for function
    immediate: boolean indicating function to be executed regardless of compilation state
    """
    def __init__(self, built_in, function, immediate, overwritable):
        self.built_in = built_in
        self.function = function
        self.immediate = immediate
        self.overwritable = overwritable

    # instantiate function as callback function
    @classmethod
    def callback(cls, f_callback, immediate=False, overwritable=False):
        return cls(True, f_callback, immediate, overwritable)

    # instantiate function with list of instructions
    @classmethod
    def instructions(cls, f_instructions, immediate=False, overwritable=True):
        return cls(False, f_instructions, immediate, overwritable)
