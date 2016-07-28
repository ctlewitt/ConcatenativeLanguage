import fileinput
import sys
from concatenative_language.function import Function
from concatenative_language.utils import append_with_num_type_cast
from concatenative_language.calculator import add, sub, mul, div, clr, prt
from concatenative_language.stack_operations import dup, drop, swap


class ConcatCompliler:
    def __init__(self):
        self.stack = []
        self.compile_mode = False
        self.compile_instruction_list = []
        self.compile_function_name = ""
        self.functions = {
            ":": Function.callback(self.enter_compile_mode, True),
            ";": Function.callback(self.exit_compile_mode, True),
            "+": Function.callback(add),
            "-": Function.callback(sub),
            "*": Function.callback(mul),
            "/": Function.callback(div),
            "clr": Function.callback(clr),
            "print": Function.callback(prt),
            "dup": Function.callback(dup),
            "drop": Function.callback(drop),
            "swap": Function.callback(swap),
            "sq": Function.instructions(["dup", "*"]),
            "fourth": Function.instructions(["sq", "sq"]),
            "add2and2": Function.instructions([2, 2, "+"])
        }

             # self.function_interpreter = Function()

    def enter_compile_mode(self, *args):
        self.compile_mode = True
        self.compile_instruction_list = []
        self.compile_function_name = ""


    def exit_compile_mode(self, *args):
        self.compile_mode = False
        self.functions[self.compile_function_name] = Function.instructions(self.compile_instruction_list)
        self.compile_function_name = ""
        self.compile_instruction_list = []
        # also want to finish saving function

    #while True:
        # line = sys.stdin.read()
    def interpret_file(self):
        for line in fileinput.input():
            for token in line.split():
                if self.compile_mode:
                    print("in compile mode")
                    # if token is immediate function, execute without compiling
                    if self.functions.get(token) is not None and self.functions[token].immediate:
                        self.execute(self.functions[token])
                    # not immediate, so compile
                    else:
                        # get function name (might need to modify this later to handle variable assignment)
                        if self.compile_function_name == "":
                            # not allowed to have : followed immediately by ;.
                            # Once in compilation mode, var/function name must be next
                            # might need to allow for reassigning variables...
                            if token in self.functions:
                                raise Exception("cannot redeclare function")
                            self.compile_function_name = token
                        else:
                            append_with_num_type_cast(self.compile_instruction_list, token)
                            print(self.compile_function_name + str(self.compile_instruction_list))
                else:
                    print("not in compile mode")
                    if token in self.functions:
                        self.execute(self.functions[token])
                    elif token.isdigit():  # need better check than this (for floats)
                        self.stack.append(int(token))  # need to convert into number


    # execute a function either as a callback or list of instructions
    def execute(self, function):
        # callback function--just execute
        if function.built_in:
            function.function(self.stack) # call function's function and execute stack
        # function with list of instructions--interpret each
        else:
            self.interpret(function)

    # go through each instruction in a list of instructions function
    def interpret(self, function):
        for word in function.function:
            if type(word) == int or type(word) == float:
                self.stack.append(word)
            else:
                self.execute(self.functions[word])




my_compiler = ConcatCompliler()
my_compiler.interpret_file()














# introspection
# or write out (add, 2) which indicates having 2 parameters
# can functions have attributes?
# python: inspect, get args back

## play with stack based languages
# forth
# factor


