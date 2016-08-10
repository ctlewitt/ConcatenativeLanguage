def create_dict(interpreter):
    interpreter.stack.append({})


def set_dict(interpreter):
    new_val = interpreter.stack.pop()
    new_key = interpreter.stack.pop()
    user_dict = interpreter.stack[-1]
    user_dict[new_key] = new_val


def get_dict(interpreter):
    index = interpreter.stack.pop()
    user_dict = interpreter.stack[-1]
    interpreter.stack.append(user_dict.get(index))

