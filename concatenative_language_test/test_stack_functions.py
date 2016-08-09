import sys
import unittest
from concatenative_language.concat_interpreter import ConcatInterpreter


class TestStackFunctions(unittest.TestCase):
    def setUp(self):
        self.my_interpreter = ConcatInterpreter()
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode to capture output")

    def test_dip_stack_and_output(self):
        self.my_interpreter.interpret_file("test_input/stack_op_input/test_dip1.txt")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "else", "incorrect output; expected 'else'")
        self.assertEqual(self.my_interpreter.stack, ["else", "something"])
