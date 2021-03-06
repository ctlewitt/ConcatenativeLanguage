from concatenative_language.function import Function
from concatenative_language.constants import DEBUG_MODE


# define:
def enter_compile_mode(compiler):
    if not compiler.block_mode:
        compiler.compile_mode = True
        compiler.need_func_name = True
        compiler.compile_function_name = ""
    # compiler.compile_mode = True
    # compiler.compile_function_name = ""


# { :
def enter_block_mode(compiler):
    # print("block depth: {}".format(compiler.block_depth))
    if compiler.block_depth == 0:
        compiler.block_mode = True
        compiler.compile_instruction_list = []
    else:
        compiler.compile_instruction_list.append(compiler.functions["{"])
    compiler.block_depth += 1


# } :
def exit_compile_and_block_mode(compiler):
    # in compile_mode (and block_mode), so creating named function
    compiler.block_depth -= 1
    if compiler.block_depth == 0:
        # print("saving function: {}".format(compiler.compile_instruction_list))
        if compiler.compile_mode:
            compiler.functions[compiler.compile_function_name] = Function.instructions(compiler.compile_instruction_list)
        # just in block_mode, so creating anonymous funtion to be pushed onto stack
        else:
            compiler.stack.append(Function.instructions(compiler.compile_instruction_list))
        if DEBUG_MODE:
            print("compiled function instruction list: {}".format(compiler.compile_instruction_list))
        # reset compiler's function name and instruction list attributes
        compiler.compile_function_name = ""
        compiler.compile_instruction_list = []
        # reset compile mode and block mode to false to exit modes and re-enter execution mode (implicitly)
        compiler.compile_mode = False
        compiler.block_mode = False
    else:
        compiler.compile_instruction_list.append(compiler.functions["}"])
