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
        return True, int(word)
    except ValueError:
        try:
            return True, float(word)
        except ValueError:
            return False, word


def cast_to_bool_if_possible(word):
    try:
        return True, bool(word)
    except ValueError:
        return False, word


def cast_to_str_if_possible(word):
    if len(word) >=2 and ((word[0] == "'" and word[-1] == "'") or (word[0] == '"' and word[-1] == '"')):
        return True, word[1:len(word)-1]
    else:
        return False, word


def append_with_type_cast(the_list, token):
    is_num, num = cast_to_number_if_possible(token)
    if is_num:
        the_list.append(num)
        return
    is_bool, bool_val = cast_to_bool_if_possible(token)
    if is_bool:
        the_list.append(bool_val)

    the_list.append(cast_to_number_if_possible(token))

