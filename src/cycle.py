#!/usr/bin/env python3

import argparse
import random

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('names',
                    type=argparse.FileType('r'),
                    help='Path to a file containing names for creating a circle of "murderer-murdered" pairs.'
                         'Only one name per line is allowed. Names may contain spaces.')

args = parser.parse_args()


def read_names_from_file(file):
    """
    Reads the provided file line by line to provide a list representation of the contained names.
    :param file: A text file containing one name per line
    :return: A list of the names contained in the provided text file
    """
    names_list = []

    for line in file:
        names_list.append(str(line).strip())

    return names_list


def create_cycle(p_names):
    """
    Creates a random mapping from murderers to people to be murdered.
    :param p_names: A list of names from which to create pairs of murderers and people to be murdered
    :return: A mapping from murderers to people to be murdered
    """
    pairs = {}
    names = p_names.copy()  # Produce no side-effects by copying list
    random.shuffle(names)

    for i in range(-1, len(names) - 1):
        murderer = names[i]
        murdered = names[i + 1]
        pairs[murderer] = murdered

    return pairs


names_list = read_names_from_file(args.names)
murder_pairs = create_cycle(names_list)
