#ConcatenativeLanguage
interpreter for concatenative programming language

I am creating a concatenative language and interpreter in Python based on Harlows Monkeys' instructions for how to do so in C in their comment on the following Reddit page:

https://www.reddit.com/r/programming/comments/4o74bq/kitten_a_concatenative_programming_language/

The interpreter can be run with runner.py.  

The interpreter can be found in the concat_interpreter.py file.  
When the interpreter is run, it breaks up the input into tokens and processes each one in order.  
There are three situations that might be encountered:
1) If the token is a value, such as an integer, string or list, it is placed onto the stack.
2) If the token is a function that has already been defined, it executes it.  (See below for an explanation of how functions are executed.)
3) If the interpreter encounters a function that needs to be compiled (indicated by "define" or "{"), it stops interpreting, as in 1 and 2 above, and begins compiling the function.
Upon completion (when a "}" has been reached), the function is either saved into the name space or pushed onto the stack (like any other value encountered, such as an integer or string) if it is an anonymous function.  

As a result, functions are first class in this language.  Functions can definen other functions (nested functions). 
Functions can also be passed as parameters to or returned by functions. 

There are two types of functions: ones written in python and ones written in the concatenative language itself.  
Regardless of the type, instead of being passed parameters or returning values, as in imperative or functional languages, 
each function has access to the stack during its execution.  The parameters are pushed onto the stack (or left there)
for the function being executed to use.  Any values intended to be returned are then pushed onto the stack.
A function's effect can be described based on the way it modifies the stack.  

Built in functions that are written in Python pop and push things to the stack, but are executed as python code (using callbacks).
Functions that are written in the language are executed just like the original input the interpreter has processed.  
Each token/word in a function is processed in order as described above.  
When a user-defined function is compiled, its tokens are appended into a list of instructions that can then be run in order any time the function is called.  

Users are encouraged to create their own functions as needed.  The core built in functions cannot be modified or overwritten, but any user-defined functions can be defined and redefined in the name-space as you develop and debug them for your use.  
For convenience, any functions defined while the interpreter is running are pickled and stored for use in the future.  If such a pickled file of saved functions is available when the interpreter is initialized, they are loaded from the pickle.  Otherwise, a core set of built in functions are loaded.  
(For more on pickling, see https://docs.python.org/3/library/pickle.html )
  
As is traditional in concatenative languages, there are named variables.  Instead, all variables are stored anonymously on the stack.
It can therefore be necessary to manipulate the stack to arrange variables in an appropriate order for use by various functions.
I recommend making heavy use of the advanced stack shuffling functions provided.  (See stack_operations.py and stack_operations.txt.)  
Using single functions (e.g., dupd) instead of sequences of functions ( { dup } dip ) can make your functions more readable and concise.  
  
Ideally, there should by very few sequences of lower level commands directly manipulating individual values on the stack.
Instead, helper functions should be defined, along with functions that are composed of those helper functions.  In the end, a program or function constructed in this way will be much more readable, containing a descriptive sequence of actions performed on the stack.
This is because functions are applied in a concatenative manner.  Each one is applied to the data in the stack in sequence, 
leaving the stack altered and ready for the next function to be applied.  

Although concatenative languages are not functional, their functions can be thought of as such.  If it helps, once a function has been tested, it can be thought of as taking a stack in a particular state and returning a "new" stack with the parameters replaced by the return values.  The old stack is never reused, so the mental model holds.  

Things that are still under development:
1) Being able to look in a file tree and load all of the user-defined functions contained therein.  (Since the pickle must be deleted and all of the functions reloaded from scratch when a new built in function is added, and since the language is still under development, this would be very useful for the time being.)
2) Although comments are available outside of functions, there are none available yet within functions, and this would be quite useful, especially when stack manipulation becomes complicated.  (I am new to this language paradigm, so this happens disappointingly often.)  
3) Better comments and documentation are needed for functions, describing their functionality, parameters, and return values.  
