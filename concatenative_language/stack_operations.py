from concatenative_language.memory import stack


def dup():
    stack.append(stack[-1])


def drop():
    stack.pop()


def swap():
    temp1 = stack.pop()
    temp2 = stack.pop()
    stack.append(temp1)
    stack.append(temp2)

