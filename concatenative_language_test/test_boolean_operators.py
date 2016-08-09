import unittest
import io
from concatenative_language.concat_interpreter import ConcatInterpreter


class TestBooleanFunctions(unittest.TestCase):
    def setUp(self):
        self.my_interpreter = ConcatInterpreter()
        self.my_interpreter.interpret_file("and.txt")
        self.my_interpreter.interpret_file("or.txt")

    def test_and_true_true_alt(self):
        test_str = "{ True } { True } and"
        self.my_interpreter.interpret_file(io.StringIO(test_str))
        self.assertEqual(self.my_interpreter.stack, [True])

    def test_and_true_true(self):
        self.my_interpreter.interpret_file("test_input/boolean_input/test_and1.txt")
        self.assertEqual(self.my_interpreter.stack, [True])

    def test_and_true_false(self):
        self.my_interpreter.interpret_file("test_input/boolean_input/test_and2.txt")
        self.assertEqual(self.my_interpreter.stack, [False])

    def test_and_false_true(self):
        self.my_interpreter.interpret_file("test_input/boolean_input/test_and3.txt")
        self.assertEqual(self.my_interpreter.stack, [False])

    def test_and_false_false(self):
        self.my_interpreter.interpret_file("test_input/boolean_input/test_and4.txt")
        self.assertEqual(self.my_interpreter.stack, [False])

    def test_or_true_true(self):
        self.my_interpreter.interpret_file("test_input/boolean_input/test_or1.txt")
        self.assertEqual(self.my_interpreter.stack, [True])

    def test_or_true_false(self):
        self.my_interpreter.interpret_file("test_input/boolean_input/test_or2.txt")
        self.assertEqual(self.my_interpreter.stack, [True])

    def test_or_false_true(self):
        self.my_interpreter.interpret_file("test_input/boolean_input/test_or3.txt")
        self.assertEqual(self.my_interpreter.stack, [True])

    def test_or_false_false(self):
        self.my_interpreter.interpret_file("test_input/boolean_input/test_or4.txt")
        self.assertEqual(self.my_interpreter.stack, [False])
