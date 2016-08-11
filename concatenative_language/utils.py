import ast
import fileinput
from concatenative_language.constants import DEBUG_MODE



def cast_to_number_if_possible(word):
    try:
        return int(word)
    except ValueError:
        return float(word)
    # will raise exception if not int or float


# checks against string "True" or "False" rather than casting to avoid accidentally casting other variables to boolean
def cast_to_bool_if_possible(word):
    if word == "True" or word is True:
        return True
    elif word == "False" or word is False:
        return False
    else:
        raise ValueError("not a boolean")


# # might need to account for case where function has saved string values without quotes
# def cast_to_str_if_possible(word, origin):
#     if (origin == "from file" and
#             len(word) >= 2 and
#             ((word[0] == "'" and word[-1] == "'") or (word[0] == '"' and word[-1] == '"'))):
#         return word[1:len(word)-1]
#     elif origin == "from function":
#         return word
#     else:
#         raise ValueError("not a str")
#     # else:
#     #     return True, word


# might need to account for case where function has saved string values without quotes
def cast_to_str_if_possible(word):
    if len(word) >= 2 and ((word[0] == "'" and word[-1] == "'") or (word[0] == '"' and word[-1] == '"')):
        return word[1:len(word)-1]
    raise ValueError("not a str")


def cast_to_list_if_possible(word):
    if word[0] == '[' and word[-1] == ']':
        return ast.literal_eval(word)
    raise ValueError("not a list")


# checks if token is a function name and returns corresponding function
# otherwise: tries to cast token string to a bool, int, float, list, or reformat to proper str and returns such
def cast_to_val(token, interpreter):
    casting_functions = [cast_to_bool_if_possible, cast_to_number_if_possible,
                         cast_to_list_if_possible, cast_to_str_if_possible]
    # token could be a function name
    if interpreter.need_func_name:
        # todo: should check to make sure that function is not a number, boolean, etc
        if DEBUG_MODE:
            print("just returning token in need_func_name situation: {}".format(token))
        return token
    if token in interpreter.functions:
        return interpreter.functions[token]
        # check if token to be cast to any variable type
        #    kwargs = {token: token, origin: origin}
    for function in casting_functions:
        try:
            return function(token)
        except ValueError:
            pass
    raise TypeError("token {} is invalid variable type or function name; could not be resolved".format(token))


# def append_with_type_cast(the_list, token, origin, functions=None):
#     casting_functions = [cast_to_bool_if_possible, cast_to_number_if_possible,
#                          cast_to_list_if_possible, cast_to_str_if_possible]
#     # if token cannot be cast, then it could be a function name
#     if functions and token in functions:
#         the_list.append(token)
#         return
#     # check if token to be cast to any variable type
# #    kwargs = {token: token, origin: origin}
#     for function in casting_functions:
#         try:
#             cast_val = function(token, origin)
#             the_list.append(cast_val)
#             return
#         except ValueError:
#             pass
#         # if successful_cast:
#         #     the_list.append(cast_val)
#         #     return
#     raise TypeError("token {} is invalid variable type or function name; could not be resolved".format(token))


# returns file-like object for interpreting
# source can be None for stdin, filename to open a file, or actual source code
def get_input(source):
    if source is None or type(source) == str:
        return fileinput.input(files=source)
    else:
        return source
