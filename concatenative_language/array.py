
def set_array(interpreter):
    new_val = interpreter.stack.pop()
    index = interpreter.stack.pop()
    arr = interpreter.stack[-1]
    arr[index] = new_val
    

def get_array(interpreter):
    index = interpreter.stack.pop()
    arr = interpreter.stack[-1]
    interpreter.stack.append(arr[index])

