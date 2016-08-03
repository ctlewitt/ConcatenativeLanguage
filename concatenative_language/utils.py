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


def cast_to_list_if_possible(word):
    return True, word
    pass

def append_with_type_cast(the_list, token, functions):
    casting_functions = [cast_to_number_if_possible, cast_to_bool_if_possible, cast_to_str_if_possible,
                         cast_to_list_if_possible]
    # check if token to be cast to any variable type
    for function in casting_functions:
        successful_cast, cast_val = function(token)
        if successful_cast:
            the_list.append(cast_val)
            return
    # if token cannot be cast, then it could be a function name
    if token in functions:
        the_list.append(token)
        return
    raise TypeError("token {} is invalid variable type or function name; could not be resolved".format(token))
