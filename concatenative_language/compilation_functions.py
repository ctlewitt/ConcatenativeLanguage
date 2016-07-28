#from concatenative_language.memory import compile_mode, compile_instruction_list
from concatenative_language.function import Function

def enter_compile_mode(compiler):
    print("in : function")
    print(compiler)
    print("Entering compile mode")
    compiler.compile_mode = True
#        print(self.compile_mode)
    compiler.compile_instruction_list = []
    compiler.compile_function_name = ""

def exit_compile_mode(compiler):
    print("in ; function")
    print(compiler)
    compiler.compile_mode = False
    compiler.functions[compiler.compile_function_name] = Function.instructions(compiler.compile_instruction_list)
    compiler.compile_function_name = ""
    compiler.compile_instruction_list = []
    # also want to finish saving function
