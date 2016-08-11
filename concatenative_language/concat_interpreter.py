from concatenative_language.function import Function
from concatenative_language.utils import get_input, cast_to_val
import concatenative_language.functions as f
import pickle
import re
import io
from concatenative_language.constants import DEBUG_MODE


class ConcatInterpreter:
    def __init__(self):
        self.stack = []
        self.functions = None
        self.load_functions()
        self.var_types = frozenset([int, float, str, bool, list])
        # variables for compiling named function modes
        self.compile_mode = False  # todo make name that more clearly indicates compiling a named function
        self.need_func_name = False
        # variables for compiling anonymous function (or block/body/conditional) modes
        self.block_mode = False
        self.block_depth = 0  # for nested functions
        # currently-compiling function details
        self.compile_function_name = ""
        self.compile_instruction_list = []

    # tries to load all builtin and user-defined functions from pickle; otherwise loads default builtin set of functions
    def load_functions(self):
        try:
            with open("saved_functions.pickle", "rb") as func_file:
                self.functions = pickle.load(func_file)
        except IOError:
            self.functions = {
                "define": Function.callback(f.enter_compile_mode, True),
                "{": Function.callback(f.enter_block_mode, True),
                "}": Function.callback(f.exit_compile_and_block_mode, True),
                "do": Function.callback(f.do),
                "if": Function.callback(f.if_conditional),
                "while": Function.callback(f.while_loop),
                "for": Function.callback(f.for_loop),
                "<": Function.callback(f.less),
                "<=": Function.callback(f.less_or_equal),
                ">": Function.callback(f.greater),
                ">=": Function.callback(f.greater_or_equal),
                "==": Function.callback(f.equal),
                "!=": Function.callback(f.not_equal),
                "is_none": Function.callback(f.is_none),
                "None": Function.callback(f.push_none),
                "+": Function.callback(f.add),
                "-": Function.callback(f.sub),
                "*": Function.callback(f.mul),
                "/": Function.callback(f.float_div),
                "//": Function.callback(f.int_div),
                "clr": Function.callback(f.clr),
                "dict_create": Function.callback(f.create_dict),
                "dict_get": Function.callback(f.get_dict),
                "dict_set": Function.callback(f.set_dict),
                "arr_append": Function.callback(f.array_append),
                "arr_pop": Function.callback(f.array_pop),
                "arr_create": Function.callback(f.array_create),
                "arr_get": Function.callback(f.array_get),
                "arr_len": Function.callback(f.array_len),
                "arr_set": Function.callback(f.array_set),
                "print": Function.callback(f.print_func),
                "dup": Function.callback(f.dup),
                "drop": Function.callback(f.drop),
                "swap": Function.callback(f.swap),
                "dip": Function.callback(f.dip),
                "rot": Function.callback(f.rot),
                "sq": Function.instructions(["dup", "*"]),
                "show_stack": Function.callback(f.print_stack)
            }


    def interpret_string(self, source_str):
        self.interpret_file(io.StringIO(source_str))

    # reads in source code, splits into tokens, ignores comments, interprets everything else
    # when done, dumps accumulated functions to-date into a pickle for retrieval in future runs
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

    # go through each word/instruction in a function's list of instructions and interpret each word
    def interpret(self, function):
        for word in function.function:
            if DEBUG_MODE:
                print("interpreting word: {}".format(word))
                print("stack before {}: {}".format(word, self.stack))
            self.interpret_word(word)
            if DEBUG_MODE:
                print("stack after{}: {}".format(word, self.stack))

    # interprets a single word;
    # immediate functions are always executed
    # if in compile mode, saves as function name or adds to list of instructions, as appropriate
    # if not compiling, executes functions and pushes other values onto the stack
    def interpret_word(self, word):
        if isinstance(word, Function) and word.immediate:  # self.functions.get(word) is not None and self.functions[word].immediate:
            self.execute(word) # self.execute(self.functions[word])
        # if in compile mode but not block, function needs name
        elif self.need_func_name:
            # Once in compilation mode, var/function name must be next token
            if word in self.functions and not self.functions[word].overwritable:
                raise Exception("cannot redeclare function {}".format(word))
            self.compile_function_name = word
            self.need_func_name = False
        # in block mode (could be in compile mode or not; doesn't matter) get each command in function
        elif self.block_mode:
            self.compile_instruction_list.append(word)
        # executing (ie, not compile or block mode)
        elif isinstance(word, Function):
            self.execute(word)
        else:
            self.stack.append(word)
