#from concatenative_language.memory import stack


def add(stack):
    stack.append(stack.pop() + stack.pop())


def sub(stack):
    stack.append(stack.pop() - stack.pop())


def mul(stack):
    stack.append(stack.pop() * stack.pop())


def div(stack):
    stack.append(stack.pop() / stack.pop())


def clr(stack):
    stack.pop()


def prt(stack):
    print(stack[-1])

