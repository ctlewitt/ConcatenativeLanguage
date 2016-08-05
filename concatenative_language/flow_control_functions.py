# do for loop

# if :takes 3 parameters: condition, true outcome, and false outcome; 0 return values
# evaluates condition and executes true/false function based on true/false outcome
def if_conditional(interpreter):
    # get parameters
    false_outcome = interpreter.stack.pop()
    true_outcome = interpreter.stack.pop()
    condition_func = interpreter.stack.pop()
    interpreter.execute(condition_func)
    condition = interpreter.stack.pop()
    # if true, do true outcome
    if condition:
        interpreter.execute(true_outcome)
    # if false, do false outcome
    else:
        interpreter.execute(false_outcome)


# while :takes 2 parameters: condition function and block; 0 return values
# recursively executes while loop's block until condition evaluates to false
def while_loop(interpreter):
    # get parameters
    block = interpreter.stack.pop()
    condition_func = interpreter.stack.pop()
    # evaluate condition function
    interpreter.execute(condition_func)
    condition = interpreter.stack.pop()
    # while condition is true, recursively repeat
    if condition:
        interpreter.execute(block)
        # leave parameters on stack for next execution
        interpreter.stack.append(condition_func)
        interpreter.stack.append(block)
        while_loop(interpreter)
    # if condition is false, do nothing


def do(interpreter):
    interpreter.execute(interpreter.stack.pop())