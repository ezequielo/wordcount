import argparse

from wordcount.package.counter import wordcount

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath', dest='filepath', help='Path to file', required=True, type=str)
    args = parser.parse_args()
    wordcount(args.filepath)
