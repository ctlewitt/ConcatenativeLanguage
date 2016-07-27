from concatenative_language.concat_compiler import functions, stack

class Function:
    '''
    Attributes:
    built_in: boolean indicating whether a function is built in (callback) or interpreted (list of instructions)
    function: callback or list of instructions (depending on c_flag) for function
    immediate: boolean indicating function to be executed regardless of compilation state
    '''
    def __init__(self, built_in, function, immediate):
        self.built_in = built_in
        self.function = function
        self.immediate = immediate

    # instantiate function as callback function
    @classmethod
    def callback(cls, f_callback, immediate=False):
        return cls(True, f_callback, immediate)

    # instantiate function with list of instructions
    @classmethod
    def instructions(cls, f_instructions=list(), immediate=False):
        return cls(False, f_instructions, immediate)

    # execute a function either as a callback
    def execute(self):
        # callback function--just execute
        if self.built_in:
            self.function()
        # function with list of instructions--interpret each
        else:
            self.interpret()

    # go through each instruction in a list of instructions function
    def interpret(self):
        for word in self.function:
            functions[word].execute()

