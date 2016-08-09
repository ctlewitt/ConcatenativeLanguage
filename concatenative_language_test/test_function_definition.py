import unittest
from concatenative_language.concat_interpreter import ConcatInterpreter
import os
import io


class TestFunctionDefinition(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("saved_functions.pickle")
        except FileNotFoundError:
            pass
        self.my_interpreter = ConcatInterpreter()

    def test_fail_with_invalid_function_name(self):
        test_str = "nonexistent_function"
        with self.assertRaises(TypeError):
            self.my_interpreter.interpret_file(io.StringIO(test_str))

    def test_named_func_def_and_exec(self):
        pass

    def test_anon_func_def_and_exec(self):
        pass

    def test_inner_anon_func_def(self):
        pass

    def test_inner_anon_func_exec(self):
        pass

    def test_inner_named_func_def(self):
        # self.my_interpreter.interpret_file("test_input/calculator_input/test_subtract1.txt")
        # self.assertEqual(self.my_interpreter.stack, [13])
        pass

    def test_inner_named_func_exec(self):
        pass

    def test_nested_nested_functions(self):
        pass
