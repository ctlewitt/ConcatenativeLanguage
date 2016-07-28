# helper to print the contents of the stack
def print_stack(stack):
    for elem in stack:
        print("e", str(elem), end="")
    print()


def is_numeric(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
