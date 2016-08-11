import sys
from concatenative_language.function import Function
from concatenative_language.utils import print_stack, get_input, cast_to_val # , append_with_type_cast
from concatenative_language.functions.calculator import add, sub, mul, div, clr, prt
from concatenative_language.functions.stack_operations import dup, drop, swap, rot, dip
from concatenative_language.functions.compilation_functions import enter_compile_mode, exit_compile_and_block_mode, enter_block_mode
from concatenative_language.functions.flow_control_functions import if_conditional, while_loop, do, for_loop
from concatenative_language.functions.comparison_operators import less, less_or_equal, greater, greater_or_equal, equal, not_equal, is_none, push_none
from concatenative_language.functions.dictionary_functions import create_dict, set_dict, get_dict
from concatenative_language.functions.array_functions import array_append, array_create, array_get, array_len, array_set, array_pop

import pickle
import re
import io
from concatenative_language.constants import DEBUG_MODE


class ConcatInterpreter:
    def __init__(self):
        self.stack = []
        self.compile_mode = False # todo make name that indicates compiling a named function;
        self.block_mode = False
        self.need_func_name = False
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
                "do": Function.callback(do),
                "if": Function.callback(if_conditional),
                "while": Function.callback(while_loop),
                "for": Function.callback(for_loop),
                "<": Function.callback(less),
                "<=": Function.callback(less_or_equal),
                ">": Function.callback(greater),
                ">=": Function.callback(greater_or_equal),
                "==": Function.callback(equal),
                "!=": Function.callback(not_equal),
                "is_none": Function.callback(is_none),
                "None": Function.callback(push_none),
                "+": Function.callback(add),
                "-": Function.callback(sub),
                "*": Function.callback(mul),
                "/": Function.callback(div),
                "clr": Function.callback(clr),
                "dict_create": Function.callback(create_dict),
                "dict_get": Function.callback(get_dict),
                "dict_set": Function.callback(set_dict),
                "arr_append": Function.callback(array_append),
                "arr_pop": Function.callback(array_pop),
                "arr_create": Function.callback(array_create),
                "arr_get": Function.callback(array_get),
                "arr_len": Function.callback(array_len),
                "arr_set": Function.callback(array_set),
                "print": Function.callback(prt),
                "dup": Function.callback(dup),
                "drop": Function.callback(drop),
                "swap": Function.callback(swap),
                "dip": Function.callback(dip),
                "rot": Function.callback(rot),
                "sq": Function.instructions(["dup", "*"]),
                "fourth": Function.instructions(["sq", "sq"]),
                "add2and2": Function.instructions([2, 2, "+"]),
                "show_stack": Function.callback(print_stack)
            }

    def interpret_file(self, source=None):
        for line in get_input(source): # fileinput.input(files=input_file):
            for token in re.findall(r'(\"[^\"]*\"|\'[^\']*\'|[\S]+|\[.^\w*\])', line):
                # beginning of comment; ignore remainder of line
                if token == "--":
                    break
                cast_token = cast_to_val(token, self)
                if DEBUG_MODE:
                    print("about to interpret word: {} aka {}".format(token, cast_token))
                self.interpret_word(cast_token)
        with open("saved_functions.pickle", "wb") as func_file:
            pickle.dump(self.functions, func_file, pickle.HIGHEST_PROTOCOL)

    # execute a function either as a callback or list of instructions
    def execute(self, function):
        # callback function--just execute
        if DEBUG_MODE:
            print("executing {}".format(function))
        if function.built_in:
            function.function(self) # call function's function and execute with stack
        # function with list of instructions--interpret each
        else:
            self.interpret(function)

    # go through each instruction in a list of instructions function
    def interpret(self, function):
        for word in function.function:
            if DEBUG_MODE:
                print("interpreting word: {}".format(word))
                print("stack before {}: {}".format(word, self.stack))
            self.interpret_word(word)
            if DEBUG_MODE:
                print("stack after{}: {}".format(word, self.stack))

    def interpret_word(self, word):
        if isinstance(word, Function) and word.immediate:  # self.functions.get(word) is not None and self.functions[word].immediate:
            self.execute(word) # self.execute(self.functions[word])
        # if in compile mode but not block, function needs name
        elif self.need_func_name:
            # Once in compilation mode, var/function name must be next token
            # might need to allow for reassigning functions (maybe if not built in, allow reassignment)...
            if word in self.functions and not self.functions[word].overwritable:
                print("trying to overwrite function {}".format(word))
                raise Exception("cannot redeclare function {}".format(word))
            self.compile_function_name = word
            self.need_func_name = False
        # in block mode (could be in compile mode or not; doesn't matter) get each command in function
        elif self.block_mode:
            self.compile_instruction_list.append(word)
        # executing (ie, not compile or block mode)
        # if word in self.functions:
        #elif word in self.functions:
        elif isinstance(word, Function):
            # self.execute(self.functions[word])
            self.execute(word)
        else:
            self.stack.append(word)
            # append_with_type_cast(self.stack, word, origin, self.functions)


