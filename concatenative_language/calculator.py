
def add(compiler):
    compiler.execute(compiler.functions['swap'])
    compiler.stack.append(compiler.stack.pop() + compiler.stack.pop())


def sub(compiler):
    compiler.execute(compiler.functions['swap'])
    compiler.stack.append(compiler.stack.pop() - compiler.stack.pop())


def mul(compiler):
    compiler.execute(compiler.functions['swap'])
    compiler.stack.append(compiler.stack.pop() * compiler.stack.pop())


def div(compiler):
    compiler.execute(compiler.functions['swap'])
    compiler.stack.append(compiler.stack.pop() / compiler.stack.pop())


def clr(compiler):
    compiler.stack.pop()


def prt(compiler):
    print(compiler.stack[-1])

