# < :removes top 2 elements from stack, compares, and pushes boolean result of comparison onto stack
def less(compiler):
    right, left = get_right_left(compiler)
    compiler.stack.append(left < right)


# > :removes top 2 elements from stack, compares, and pushes boolean result of comparison onto stack
def greater(compiler):
    right, left = get_right_left(compiler)
    compiler.stack.append(left > right)


# <= :removes top 2 elements from stack, compares, and pushes boolean result of comparison onto stack
def less_or_equal(compiler):
    right, left = get_right_left(compiler)
    compiler.stack.append(left <= right)


# >= :removes top 2 elements from stack, compares, and pushes boolean result of comparison onto stack
def greater_or_equal(compiler):
    right, left = get_right_left(compiler)
    compiler.stack.append(left >= right)


# == :removes top 2 elements from stack, compares, and pushes boolean result of comparison onto stack
def equal(compiler):
    right, left = get_right_left(compiler)
    print("ans to ==: {}".format(left == right))
    compiler.stack.append(left == right)


# != :removes top 2 elements from stack, compares, and pushes boolean result of comparison onto stack
def not_equal(compiler):
    right, left = get_right_left(compiler)
    compiler.stack.append(left != right)


# helper: returns top and next value from stack as right and left values respectively for comparison
def get_right_left(compiler):
    return compiler.stack.pop(), compiler.stack.pop()