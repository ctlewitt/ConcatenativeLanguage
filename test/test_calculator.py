import unittest
from concatenative_language.concat_interpreter import ConcatInterpreter


class TestCalculatorFunctions(unittest.TestCase):
    def setUp(self):
        self.my_interpreter = ConcatInterpreter()

    def test_add(self):
        self.my_interpreter.interpret_file("test_input/calculator_input/test_add1.txt")
        self.assertEqual(self.my_interpreter.stack, [4])

    def test_subtract_pos(self):
        self.my_interpreter.interpret_file("test_input/calculator_input/test_subtract1.txt")
        self.assertEqual(self.my_interpreter.stack, [13])

    def test_subtract_neg(self):
        self.my_interpreter.interpret_file("test_input/calculator_input/test_subtract2.txt")
        self.assertEqual(self.my_interpreter.stack, [-13])