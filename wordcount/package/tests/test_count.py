import unittest
import os
from wordcount.package.counter import _count


TEST_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_OK = 'resources/example.txt'
FILE_SAME = 'resources/example_same_words.txt'
FILE_DIFF = 'resources/example_diff_words.txt'


class TestsCount(unittest.TestCase):

    def test_ok(self):
        filepath = os.path.join(TEST_DIR, FILE_OK)
        word_counter = _count(filepath)
        self.assertTrue(word_counter['Hello'], 1)
        self.assertTrue(word_counter['is'], 1)
        self.assertTrue(word_counter['example'], 3)

    def test_different_files_same_words(self):
        filepath_1 = os.path.join(TEST_DIR, FILE_OK)
        filepath_2 = os.path.join(TEST_DIR, FILE_SAME)
        wc_1 = _count(filepath_1)
        wc_2 = _count(filepath_2)
        self.assertTrue(wc_1 - wc_2 == wc_2 - wc_1)

    def test_different_files_different_words(self):
        filepath_1 = os.path.join(TEST_DIR, FILE_OK)
        filepath_2 = os.path.join(TEST_DIR, FILE_DIFF)
        wc_1 = _count(filepath_1)
        wc_2 = _count(filepath_2)
        self.assertFalse(wc_1 - wc_2 == wc_2 - wc_1)
