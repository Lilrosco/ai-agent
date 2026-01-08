# test_get_file_content.py

import unittest
from config import MAX_CHARS
from functions.get_file_content import get_file_content

class TestGetFileInfo(unittest.TestCase):

    def test_get_file_content_truncates(self):
        file_path = "lorem.txt"
        result = get_file_content("calculator", file_path)
        print(result)
        self.assertTrue(len(result) > 10_000)
        self.assertTrue(f'[...File "{file_path}" truncated at {MAX_CHARS} characters]' in result)

    def test_get_file_content_reads_file(self):
        result = get_file_content("calculator", "main.py")
        print(result)
        self.assertTrue(len(result) <= 10_000)
        self.assertFalse(f'truncated at {MAX_CHARS} characters]' in result)

    def test_get_file_content_reads_file_in_sub_dir(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
        self.assertTrue(len(result) <= 10_000)
        self.assertFalse(f'truncated at {MAX_CHARS} characters]' in result)

    def test_get_file_content_errors_when_outside_working_dir(self):
        file_path = "/bin/cat"
        result = get_file_content("calculator", file_path)
        print(result)
        self.assertTrue(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' in result)

    def test_get_file_content_errors_when_file_missing(self):
        file_path = "pkg/does_not_exist.py"
        result = get_file_content("calculator", file_path)
        print(result)
        self.assertTrue(f'Error: File not found or is not a regular file: "{file_path}"' in result)


if __name__ == "__main__":
    unittest.main()
