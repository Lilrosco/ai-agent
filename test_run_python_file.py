# test_run_python_file.py

import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):

    def test_run_calc_python_with_no_args(self):
        result = run_python_file("calculator", "main.py")
        print(result)
        self.assertTrue('Usage: python main.py "<expression>"' in result)

    def test_run_calc_python_with_args(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)
        self.assertTrue('STDOUT:' in result)
        self.assertTrue('expression": "3 + 5"' in result)
    
    def test_run_calc_python_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)
        self.assertTrue("OK" in result)
        self.assertFalse("FAILED" in result)
        self.assertFalse("failures=" in result)
    
    def test_fails_when_outside_working_dir(self):
        result = run_python_file("calculator", "../main.py")
        print(result)
        self.assertTrue("outside the permitted working directory" in result)
    
    def test_fails_when_file_does_not_exist(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        self.assertTrue("does not exist or is not a regular file" in result)
    
    def test_fails_with_non_python_file(self):
        result = run_python_file("calculator", "lorem.txt")
        print(result)
        self.assertTrue("is not a Python file" in result)


if __name__ == "__main__":
    unittest.main()
