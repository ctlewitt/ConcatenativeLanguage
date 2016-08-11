# num num -> num
# takes two numbers and returns their sum
def add(interpreter):
    interpreter.execute(interpreter.functions['swap'])
    interpreter.stack.append(interpreter.stack.pop() + interpreter.stack.pop())

# num num -> num
# takes two numbers and returns the different between the first and the second (deepest num first)
def sub(interpreter):
    interpreter.execute(interpreter.functions['swap'])
    interpreter.stack.append(interpreter.stack.pop() - interpreter.stack.pop())


def mul(interpreter):
    interpreter.execute(interpreter.functions['swap'])
    interpreter.stack.append(interpreter.stack.pop() * interpreter.stack.pop())

# num num -> int (could be rounded float if either num was a float)
# takes two numbers and returns the first divided by the second (deepest num first)
# uses integer division
def int_div(interpreter):
    interpreter.execute(interpreter.functions['swap'])
    interpreter.stack.append(interpreter.stack.pop() // interpreter.stack.pop())


# num num -> float
# takes two numbers and returns the first divided by the second (deepest num first)
# uses floating point division
def float_div(interpreter):
    interpreter.execute(interpreter.functions['swap'])
    interpreter.stack.append(interpreter.stack.pop() / interpreter.stack.pop())


# entire_stack -> []
# removes everything from the stack
# warning: very destructive
def clr(interpreter):
    interpreter.stack = []
