# () -> array
# Adds an empty array to the stack
def array_create(interpreter):
    interpreter.stack.append([])


# array int val -> array
# Takes an array, index, and new value and updates the index position with the new value
def array_set(interpreter):
    new_val = interpreter.stack.pop()
    index = interpreter.stack.pop()
    arr = interpreter.stack[-1]
    arr[index] = new_val


# array int -> array val
# Takes an array and index, and returns the array and the value at the index position in array
def array_get(interpreter):
    index = interpreter.stack.pop()
    arr = interpreter.stack[-1]
    interpreter.stack.append(arr[index])


# array -> array int
# Takes an array and returns the array and its length
def array_len(interpreter):
    arr = interpreter.stack[-1]
    interpreter.stack.append(len(arr))


# array val -> array
# Takes an array and a value to be appended and returns the array with the value appended
def array_append(interpreter):
    append_val = interpreter.stack.pop()
    arr = interpreter.stack[-1]
    arr.append(append_val)


# array -> array val
# Takes an array and removes the last value, pushing it onto the stack
def array_pop(interpreter):
    arr = interpreter.stack[-1]
    last_val = arr.pop()
    interpreter.stack.append(last_val)