import os
import string
import sys
import time

from collections import Counter


ALLOWED_EXTENSIONS = ['.txt']
TRANSLATOR = str.maketrans(string.punctuation, ' ' * len(string.punctuation))


def _remove_punctuation(line):
    """
    Removes punctuation chars in a String containing a line
    :param line: String
    :return: String without punctuation chars
    """
    return line.translate(TRANSLATOR)


def _process_line(line):
    """
    Cleans a line and returns a list of words
    :param line: String representing a line
    :return: A List of words
    """
    clean_line = _remove_punctuation(line)
    return clean_line.split()


def _check_file(filepath):
    """
    Checks a filepath, can be upgraded with file extensions
    :param filepath: String containing a filepath
    :return: Boolean if file exists
    """
    filename, extension = os.path.splitext(filepath)
    return os.path.exists(filepath) and extension in ALLOWED_EXTENSIONS


def _count(filepath):
    """
    Performs the counting operation over the lines of a file
    :param filepath: Filepath
    :return: Counter with word frequency
    """
    word_counter = Counter()
    line_count = 0
    try:
        with open(filepath) as f:
            for line in f:
                print(f'Processing line {str(line_count)}')
                words = _process_line(line)
                word_counter.update(words)
                line_count = line_count + 1
        return word_counter
    except IOError:
        sys.exit('Something when wrong while reading the file')
    except Exception:
        sys.exit(f'Something when wrong while processing line {line_count}. Please check the file content.')


def wordcount(filepath):

    start_time = time.time()
    print('Starting the word count...')

    # file check
    if not _check_file(filepath):
        sys.exit(f'Something went wrong while checking the file. Make sure the filepath is correct and '
                 f'the file extension is one of [{",".join(ALLOWED_EXTENSIONS)}]')

    # read file and count in lines
    print('Starting count..')
    counter = _count(filepath)

    # display results
    print(counter.most_common())
    end_time = time.time()
    print(f'Word count completed. Took: {end_time - start_time} seconds')

