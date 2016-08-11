import unittest
from concatenative_language import ConcatInterpreter


class ConcatInterpreterTestCase(unittest.TestCase):

    def setUp(self):
        self.my_interpreter = ConcatInterpreter()

    def assertStackEqual(self, expected_stack):
        self.assertEqual(self.my_interpreter.stack, expected_stack)
