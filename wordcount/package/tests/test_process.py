import unittest
import string


from wordcount.package.counter import _process_line

LINE = 'This! is,a line)'


class TestsPorcess(unittest.TestCase):

    def test_ok(self):
        list_of_words = _process_line(LINE)
        self.assertEqual(len(list_of_words), 4)
        self.assertTrue('This' in list_of_words)
        self.assertTrue('is' in list_of_words)
        self.assertTrue('a' in list_of_words)
        self.assertTrue('line' in list_of_words)

    def test_only_punctuation(self):
        list_of_words = _process_line(string.punctuation)
        self.assertEqual(len(list_of_words), 0)
