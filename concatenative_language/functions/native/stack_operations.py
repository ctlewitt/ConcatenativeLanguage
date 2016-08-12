#  add function bi()


# entire_stack -> []
# removes everything from the stack
# warning: very destructive
def clr(interpreter):
    interpreter.stack = []


def dup(compiler):
    compiler.stack.append(compiler.stack[-1])


def drop(compiler):
    compiler.stack.pop()


def swap(compiler):
    temp1 = compiler.stack.pop()
    temp2 = compiler.stack.pop()
    compiler.stack.append(temp1)
    compiler.stack.append(temp2)


def rot(interpreter):
    temp1 = interpreter.stack.pop()
    temp2 = interpreter.stack.pop()
    temp3 = interpreter.stack.pop()
    interpreter.stack.append(temp2)
    interpreter.stack.append(temp1)
    interpreter.stack.append(temp3)


def dip(compiler):
    # get function dip will execute
    func = compiler.stack.pop()
    # remove top of stack temporarily
    top = compiler.stack.pop()
    # execute function on (what were) elements just below the top of the stack
    compiler.execute(func)
    # replace the top of the stack
    compiler.stack.append(top)
