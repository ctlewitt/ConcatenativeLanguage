#  add additional functions bi, dip


def dup(compiler):
    compiler.stack.append(compiler.stack[-1])


def drop(compiler):
    compiler.stack.pop()


def swap(compiler):
    temp1 = compiler.stack.pop()
    temp2 = compiler.stack.pop()
    compiler.stack.append(temp1)
    compiler.stack.append(temp2)

