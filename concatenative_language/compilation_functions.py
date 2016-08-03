from concatenative_language.function import Function


def enter_compile_mode(compiler):
    compiler.compile_mode = True
    compiler.compile_function_name = ""


def enter_block_mode(compiler):
    compiler.block_mode = True
    compiler.compile_instruction_list = []


def exit_compile_and_block_mode(compiler):
    # in compile_mode (and block_mode), so creating named function
    if compiler.compile_mode:
        compiler.functions[compiler.compile_function_name] = Function.instructions(compiler.compile_instruction_list)
    # just in block_mode, so creating anonymous funtion to be pushed onto stack
    else:
        compiler.stack.append(Function.instructions(compiler.compile_instruction_list))
    # reset compiler's function name and instruction list attributes
    compiler.compile_function_name = ""
    compiler.compile_instruction_list = []
    # reset compile mode and block mode to false to exit modes and re-enter execution mode (implicitly)
    compiler.compile_mode = False
    compiler.block_mode = False
