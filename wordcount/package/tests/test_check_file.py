import unittest
import os
from wordcount.package.counter import _check_file


TEST_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_OK = 'resources/example.txt'
FILE_WRONG_EXT = 'resources/example.doc'


class TestsCheckFile(unittest.TestCase):

    def test_check_file_ok(self):
        filepath = os.path.join(TEST_DIR, FILE_OK)
        self.assertTrue(_check_file(filepath))

    def test_check_file_does_not_exist(self):
        filepath = os.path.join(TEST_DIR, FILE_WRONG_EXT)
        self.assertFalse(_check_file(filepath))

    def test_check_file_unsupported_extension(self):
        filepath = os.path.join(TEST_DIR, 'my_file_.txt')
        self.assertFalse(_check_file(filepath))
