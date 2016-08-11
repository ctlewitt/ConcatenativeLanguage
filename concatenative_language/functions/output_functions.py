# see also print_and_burn function implemented in the language,
# which prints the most recent value on the stack and removes it


# val -> val
# prints the last item on the stack with no side effects
def print_func(interpreter):
    print(interpreter.stack[-1])


# stack -> stack
# non-destructively prints the contents of the stack
def print_stack(interpreter):
    for elem in interpreter.stack:
        print("{}, ".format(elem), end="")
    print()

