# test_get_file_content.py

import unittest
from functions.write_file import write_file

class TestGetFileInfo(unittest.TestCase):

    def test_write_file_succeeds(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
        self.assertTrue("28 characters written" in result)

    def test_write_file_succeeds_with_sub_dir(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
        self.assertTrue("26 characters written" in result)

    def test_write_file_errors_when_outside_working_dir(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        self.assertTrue("outside the permitted working directory" in result)

    def test_write_file_errors_when_only_providing_dir(self):
        result = write_file("calculator", "pkg", "this should not be allowed as well")
        print(result)
        self.assertTrue("it is a directory" in result)


if __name__ == "__main__":
    unittest.main()
