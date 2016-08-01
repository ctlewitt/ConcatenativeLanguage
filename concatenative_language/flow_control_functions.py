def if_conditional(compiler):
    true_outcome = compiler.stack().pop()
    false_outcome = compiler.stack().pop()
    condition = compiler.stack().pop()
    if condition:
        compiler.execute(true_outcome)
    else:
        compiler.execute(false_outcome)

#want to do while also