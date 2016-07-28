# from concatenative_language.memory import stack


def dup(stack):
    stack.append(stack[-1])


def drop(stack):
    stack.pop()


def swap(stack):
    temp1 = stack.pop()
    temp2 = stack.pop()
    stack.append(temp1)
    stack.append(temp2)

