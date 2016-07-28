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


def cast_to_number_if_possible(word):
    try:
        return int(word)
    except ValueError:
        try:
            return float(word)
        except ValueError:
            return word


def append_with_num_type_cast(the_list, token):
    the_list.append(cast_to_number_if_possible(token))

