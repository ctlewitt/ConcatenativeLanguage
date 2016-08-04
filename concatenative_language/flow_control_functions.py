# do for loop

# if :takes 3 parameters: condition, true outcome, and false outcome; 0 return values
# evaluates condition and executes true/false function based on true/false outcome
def if_conditional(compiler):
    # get parameters
    false_outcome = compiler.stack.pop()
    true_outcome = compiler.stack.pop()
    condition = compiler.stack.pop()
    # if true, do true outcome
    if condition:
        compiler.execute(true_outcome)
    # if false, do false outcome
    else:
        compiler.execute(false_outcome)


# while :takes 2 parameters: condition function and block; 0 return values
# recursively executes while loop's block until condition evaluates to false
def while_loop(compiler):
    # get parameters
    block = compiler.stack.pop()
    condition_func = compiler.stack.pop()
    # evaluate condition function
    compiler.execute(condition_func)
    condition = compiler.stack.pop()
    # while condition is true, recursively repeat
    if condition:
        print("while looping")
        compiler.execute(block)
        # leave parameters on stack for next execution
        compiler.stack.append(condition_func)
        compiler.stack.append(block)
        while_loop(compiler)
    # if condition is false, do nothing
