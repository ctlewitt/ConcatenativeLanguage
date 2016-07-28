import fileinput
import sys
from concatenative_language.function import functions
from concatenative_language.memory import stack, compile_mode, compile_instruction_list


# dict of functions
# functions = {
#     "+": Function.callback(add),
#     "-": Function.callback(sub),
#     "*": Function.callback(mul),
#     "/": Function.callback(div),
#     "clr": Function.callback(clr),
#     "print": Function.callback(prt)
# }


#while True:
    # line = sys.stdin.read()
for line in fileinput.input():
    for token in line.split():
        if compile_mode:
            compile_instruction_list.append(token)
        else:
            if token in functions:
                functions[token].execute()
    #           print_stack(stack)
            elif token.isdigit():  # need better check than this (for floats)
                stack.append(int(token))  # need to convert into number



# introspection
# or write out (add, 2) which indicates having 2 parameters
# can functions have attributes?
# python: inspect, get args back

## play with stack based languages
# forth
# factor


