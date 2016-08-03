import fileinput
import sys
from concatenative_language.function import Function
from concatenative_language.utils import append_with_type_cast
from concatenative_language.calculator import add, sub, mul, div, clr, prt
from concatenative_language.stack_operations import dup, drop, swap
from concatenative_language.compilation_functions import enter_compile_mode, exit_compile_and_block_mode, enter_block_mode
from concatenative_language.flow_control_functions import if_conditional
import pickle
import re

class ConcatCompliler:
    def __init__(self):
        self.stack = []
        self.compile_mode = False
        self.block_mode = False
        self.block_depth = 0
        self.compile_instruction_list = []
        self.compile_function_name = ""
        self.functions = None
        self.load_functions()
        self.var_types = frozenset([int, float, str, bool, list])

    def load_functions(self):
        try:
            with open("saved_functions.pickle", "rb") as func_file:
                self.functions = pickle.load(func_file)
        except IOError:
            self.functions = {
                "define": Function.callback(enter_compile_mode, True),
                "{": Function.callback(enter_block_mode, True),
                "}": Function.callback(exit_compile_and_block_mode, True),
                "if": Function.callback(if_conditional),
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



    # while True:
        # line = sys.stdin.read()
    def interpret_file(self):
        for line in fileinput.input():
            for token in re.findall(r'(\"[^\"]*\"|\'[^\']*\'|[\S]+|\[.^\w*\])', line):
                # if token is immediate function, execute without compiling
                if self.functions.get(token) is not None and self.functions[token].immediate:
                    self.execute(self.functions[token])
                # if in compile mode but not block, function needs name
                elif self.compile_mode and not self.block_mode:
                    # Once in compilation mode, var/function name must be next token
                    # might need to allow for reassigning functions (maybe if not built in, allow reassignment)...
                    if token in self.functions:
                        raise Exception("cannot redeclare function")
                    self.compile_function_name = token
                # in block mode (could be in compile mode or not; doesn't matter) get each command in function
                elif self.block_mode:
                    append_with_type_cast(self.compile_instruction_list, token, self.functions)
                # executing (ie, not compile or block mode)
                else:
                    if token in self.functions:
                        self.execute(self.functions[token])
                    else:
                        append_with_type_cast(self.stack, token, self.functions)
        with open("saved_functions.pickle", "wb") as func_file:
            pickle.dump(self.functions, func_file, pickle.HIGHEST_PROTOCOL)

    # execute a function either as a callback or list of instructions
    def execute(self, function):
        # callback function--just execute
        if function.built_in:
            function.function(self) # call function's function and execute stack
        # function with list of instructions--interpret each
        else:
            self.interpret(function)

    # go through each instruction in a list of instructions function
    def interpret(self, function):
        for word in function.function:
            if word in self.functions:
                self.execute(self.functions[word])
            else:
                self.stack.append(word)


my_compiler = ConcatCompliler()
my_compiler.interpret_file()
