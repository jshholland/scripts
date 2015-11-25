#!/usr/bin/env python3

import argparse
import random
import string
import sys


def good_word(word):
    return all(c in string.ascii_lowercase for c in word)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', type=int, default=5)
    parser.add_argument('-n', '--number', type=int, default=10)
    parser.add_argument('-w', '--words', default='/usr/share/dict/words')

    return parser.parse_args(argv)


def main(argv):
    args = parse_args(argv)

    with open(args.words, 'r') as words_file:
        all_words = [word.strip() for word in words_file.readlines() if good_word(word.strip())]

    for i in range(args.number):
        print(' '.join(random.choice(all_words) for j in range(args.length)))

if __name__ == '__main__':
    main(sys.argv[1:])
