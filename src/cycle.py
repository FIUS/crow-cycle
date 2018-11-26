#!/usr/bin/env python3

import argparse

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


names_list = read_names_from_file(args.names)
