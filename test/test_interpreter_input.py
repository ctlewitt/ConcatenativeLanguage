import unittest
import io
from concatenative_language.concat_interpreter import ConcatInterpreter


class TestInterpreterInput(unittest.TestCase):
    def test_stringinput_fileinput_equivalent(self):
        # creating parallel interpreters
        my_interpreter1 = ConcatInterpreter()
        my_interpreter2 = ConcatInterpreter()
        test_str = "1 2 3 + +"
        # interpreting input as string
        my_interpreter1.interpret_string(test_str)
        stack_w_str_input = my_interpreter1.stack
        # interpreting input as file
        my_interpreter2.interpret_file(io.StringIO(test_str))
        stack_w_file_input = my_interpreter2.stack
        # check that resulting stacks are the same
        self.assertEqual(stack_w_file_input, stack_w_str_input,
                         "interpreter with string input should produce same result as interpreter with file input")
