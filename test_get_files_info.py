# test_get_files_info.py

import unittest
from functions.get_files_info import get_files_info


class TestGetFileInfo(unittest.TestCase):

    def test_files_info_calculator(self):
        result = get_files_info("calculator", ".")
        print("Result for current directory:\n" + result + "\n")
        self.assertTrue("main.py" in result)
        self.assertTrue("tests.py" in result)
        self.assertTrue("pkg" in result)

    def test_files_info_cal_pkg(self):
        result = get_files_info("calculator", "pkg")
        print("Result for current directory:\n" + result + "\n")
        self.assertTrue("calculator.py" in result)
        self.assertTrue("render.py" in result)

    def test_files_info_bin(self):
        result = get_files_info("calculator", "/bin")
        print("Result for current directory:\n" + result + "\n")
        self.assertTrue('Error: Cannot list "/bin" as it is outside the permitted working directory' in result)

    def test_files_info_root(self):
        result = get_files_info("calculator", "../")
        print("Result for current directory:\n" + result + "\n")
        self.assertTrue('Error: Cannot list "../" as it is outside the permitted working directory' in result)


if __name__ == "__main__":
    unittest.main()
