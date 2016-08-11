
def array_set(interpreter):
    new_val = interpreter.stack.pop()
    index = interpreter.stack.pop()
    arr = interpreter.stack[-1]
    arr[index] = new_val


def array_get(interpreter):
    index = interpreter.stack.pop()
    arr = interpreter.stack[-1]
    interpreter.stack.append(arr[index])


def array_create(interpreter):
    interpreter.stack.append([])


def array_len(interpreter):
    arr = interpreter.stack[-1]
    interpreter.stack.append(len(arr))


def array_append(interpreter):
    append_val = interpreter.stack.pop()
    arr = interpreter.stack[-1]
    arr.append(append_val)


def array_pop(interpreter):
    arr = interpreter.stack[-1]
    last_val = arr.pop()
    interpreter.stack.append(last_val)