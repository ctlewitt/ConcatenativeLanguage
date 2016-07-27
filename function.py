class Function:
    '''
    Attributes:
    c_flag: boolean indicating callback or list of instructions
    function: callback or list of instructions (depending on c_flag) for function
    immediate: boolean indicating function to be executed regardless of compilation state
    '''
    def __init__(self, c_flag, function, immediate):
        self.c_flag = c_flag
        self.function = function
        self.immediate = immediate

    @classmethod
    def callback(cls, f_callback, immediate=False):
        return cls(True, f_callback, immediate)

    @classmethod
    def instructions(cls, f_instructions=[], immediate=False):
        return cls(False, f_instructions, immediate)