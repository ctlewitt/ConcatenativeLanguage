import fileinput
import sys
from calculator import add, sub, mul, div, clr, prt

stack = list()


#dict of callbacks
function = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "clr": clr,
    "print": prt

}




def print_stack(stack):
    for elem in stack:
        print("e", str(elem), end="")
    print()



#while True:
    # line = sys.stdin.read()
for line in fileinput.input():
    for token in line.split():
        if token in function:
            function[token](stack)
#                print_stack(stack)
        elif token.isdigit():  # need better check than this (for floats)
            stack.append(int(token))  # need to convert into number



# introspection
# or write out (add, 2) which indicates having 2 parameters
# can functions have attributes?
# python: inspect, get args back

## play with stack based languages
# forth
# factor
