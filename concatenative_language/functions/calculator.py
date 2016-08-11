
def add(interpreter):
    interpreter.execute(interpreter.functions['swap'])
    interpreter.stack.append(interpreter.stack.pop() + interpreter.stack.pop())


def sub(interpreter):
    interpreter.execute(interpreter.functions['swap'])
    interpreter.stack.append(interpreter.stack.pop() - interpreter.stack.pop())


def mul(interpreter):
    interpreter.execute(interpreter.functions['swap'])
    interpreter.stack.append(interpreter.stack.pop() * interpreter.stack.pop())


def div(interpreter):
    interpreter.execute(interpreter.functions['swap'])
    interpreter.stack.append(interpreter.stack.pop() // interpreter.stack.pop())
    # todo: make integer division and float division separate functions


def clr(interpreter):
    interpreter.stack.pop()


def prt(interpreter):
    print(interpreter.stack[-1])

