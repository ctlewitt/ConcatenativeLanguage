from concatenative_language import memory


def enter_compile_mode():
    memory.compile_mode = True
    memory.compile_instruction_list = []


def exit_compile_mode():
    memory.compile_mode = False
    # also want to finish saving function