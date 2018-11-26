#!/usr/bin/env python3

import argparse
import csv
import random
import sys

# If you change the arguments, please update the usage section in README.md
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input',
                    type=argparse.FileType('r'),
                    help='Path to the file containing names for creating a circle of "murderer-murdered" pairs. '
                         'Only one name per line is allowed. Names may contain spaces. '
                         'If not specified, the input is read from the standard input.')
parser.add_argument('-o', '--output',
                    type=argparse.FileType('w'),
                    help='Path to the output file. '
                         'If not specified, the output is written to the standard output.')
args = parser.parse_args()


def read_lines_from_input(file):
    """
    Reads the provided file line by line to provide a list representation of the contained names.
    :param file: A text file containing one name per line. If it's None, the input is read from the standard input.
    :return: A list of the names contained in the provided text file
    """
    if file is None:
        file = sys.stdin.readlines()
    return map(lambda l: l.strip(), file)


def create_cycle(p_names):
    """
    Creates a random mapping from murderers to people to be murdered.
    :param p_names: A list of names from which to create pairs of murderers and people to be murdered
    :return: A mapping from murderers to people to be murdered
    """
    pairs = []
    # Produce no side-effects by copying list
    names = [name for name in p_names]
    random.shuffle(names)

    for i in range(-1, len(names) - 1):
        murder_src = names[i]
        murder_dst = names[i + 1]
        pairs.append((murder_src, murder_dst))

    random.shuffle(pairs)
    return pairs


def pairs_to_csv(pair_list):
    for first, second in pair_list:
        yield "{},{}".format(first, second)


def write_lines_to_output(file, lines):
    if file is None:
        file = sys.stdout
    for l in lines:
        file.write(l)
        file.write('\n')


names_list = read_lines_from_input(args.input)
murder_pairs = create_cycle(names_list)
murder_csv = pairs_to_csv(murder_pairs)
write_lines_to_output(args.output, murder_csv)
