from test import ConcatInterpreterTestCase


class TestBooleanFunctions(ConcatInterpreterTestCase):
    def setUp(self):
        super().setUp()
        self.my_interpreter.interpret_file("concatenative_language/functions/and.da")
        self.my_interpreter.interpret_file("concatenative_language/functions/or.da")

    def test_and_true_true(self):
        self.my_interpreter.interpret_string("{ True } { True } and")
        self.assertStackEqual([True])

    def test_and_true_false(self):
        self.my_interpreter.interpret_string("{ True } { False } and")
        self.assertStackEqual([False])

    def test_and_false_true(self):
        self.my_interpreter.interpret_string("{ False } { True } and")
        self.assertStackEqual([False])

    def test_and_false_false(self):
        self.my_interpreter.interpret_string("{ False } { False } and")
        self.assertStackEqual([False])

    def test_or_true_true(self):
        self.my_interpreter.interpret_string("{ True } { True } or")
        self.assertEqual(self.my_interpreter.stack, [True])

    def test_or_true_false(self):
        self.my_interpreter.interpret_string("{ True } { False } or")
        self.assertEqual(self.my_interpreter.stack, [True])

    def test_or_false_true(self):
        self.my_interpreter.interpret_string("{ False } { True } or")
        self.assertEqual(self.my_interpreter.stack, [True])

    def test_or_false_false(self):
        self.my_interpreter.interpret_string("{ False } { False } or")
        self.assertEqual(self.my_interpreter.stack, [False])


