import unittest
from concatenative_language.concat_interpreter import ConcatInterpreter


class TestCalculatorFunctions(unittest.TestCase):
    def setUp(self):
        self.my_interpreter = ConcatInterpreter()

    def test_add(self):
        self.my_interpreter.interpret_string("2 2 +")
        self.assertEqual(self.my_interpreter.stack, [4])

    def test_subtract_pos(self):
        self.my_interpreter.interpret_string("15 2 -")
        self.assertEqual(self.my_interpreter.stack, [13])

    def test_subtract_neg(self):
        self.my_interpreter.interpret_string("2 15 -")
        self.assertEqual(self.my_interpreter.stack, [-13])

    def test_multiply(self):
        self.my_interpreter.interpret_string("4 5 *")
        self.assertEqual(self.my_interpreter.stack, [20])

    def test_integer_division_int_ans(self):
        self.my_interpreter.interpret_string("20 4 //")
        self.assertEqual(self.my_interpreter.stack, [5])

    def test_integer_division_rounded_ans(self):
        self.my_interpreter.interpret_string("3 2 //")
        self.assertEqual(self.my_interpreter.stack, [1])

    def test_floating_point_division(self):
        self.my_interpreter.interpret_string("1 2 /")
        self.assertEqual(self.my_interpreter.stack, [0.5])