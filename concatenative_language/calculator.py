from concatenative_language.memory import stack

def add():
    stack.append(stack.pop() + stack.pop())


def sub():
    stack.append(stack.pop() - stack.pop())


def mul():
    stack.append(stack.pop() * stack.pop())


def div():
    stack.append(stack.pop() / stack.pop())


def clr():
    stack.pop()


def prt():
    print(stack[-1])

