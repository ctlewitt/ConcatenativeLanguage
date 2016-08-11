from concatenative_language.concat_interpreter import ConcatInterpreter
import sys


def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = None
    my_interpreter = ConcatInterpreter()
    my_interpreter.interpret_file(filename)

if __name__ == "__main__":
    main()