import ast
import fileinput


# returns file-like object for interpreting
# source can be None for stdin, filename to open a file, or actual source code
def get_input(source):
    if source is None or type(source) == str:
        return fileinput.input(files=source)
    else:
        return source


# checks if token is a function name and returns corresponding function
# otherwise: tries to convert token to a bool, int, float, list, or reformat to proper str
# and returns such
def cast_to_val(token, interpreter):
    # token could be a function name for a function currently being defined
    # e.g., func_name in "define func_name { body }"
    if interpreter.need_func_name:
        return token
    # token corresponds with already-existing function; return function
    if token in interpreter.functions:
        return interpreter.functions[token]
    # check if token could be a bool, int, float, list, or str and return "cast" value
    casting_functions = [cast_to_bool_if_possible, cast_to_number_if_possible,
                         cast_to_list_if_possible, cast_to_str_if_possible]
    for function in casting_functions:
        try:
            return function(token)
        except ValueError:
            pass
    # token was not a function name or valid variable; raise exception to notify programmer
    raise TypeError("token {} is invalid variable type or function name; could not be resolved".format(token))


# helper for cast_to_val:
# casts a value to an int or a float if possible;
# raises exception if neither int nor float
def cast_to_number_if_possible(word):
    try:
        return int(word)
    except ValueError:
        return float(word)


# helper for cast_to_val:
# "casts" a value to True or False if appropriate; checks against string or value rather than aggressively casting
# raises exception if not a boolean
def cast_to_bool_if_possible(word):
    if word == "True" or word is True:
        return True
    elif word == "False" or word is False:
        return False
    else:
        raise ValueError("not a boolean")


# helper for cast_to_val:
# "casts" a value to string, removing leading and trailing quotation marks;
# raises an exception if not a string
def cast_to_str_if_possible(word):
    if len(word) >= 2 and ((word[0] == "'" and word[-1] == "'") or (word[0] == '"' and word[-1] == '"')):
        return word[1:len(word)-1]
    raise ValueError("not a str")


# helper for cast_to_val:
# "casts" a value to list, using ast.literal_eval (cannot handle non-literals, unfortunately, so no lists of functions)
# raises an exception if not a list
def cast_to_list_if_possible(word):
    if word[0] == '[' and word[-1] == ']':
        return ast.literal_eval(word)
    raise ValueError("not a list")
