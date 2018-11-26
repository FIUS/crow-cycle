#!/usr/bin/env python3

import argparse
import random
import csv

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


def print_pairs(pairs):
    for key in pairs.keys():
        print("%s ---[kills]---> %s" % (key, pairs[key]))


def save_pairs(pairs):
    with open('murder_pairs.csv', 'w') as f:
        for key in pairs.keys():
            f.write("%s,%s\n" % (key, pairs[key]))


def save_pairs_seperated(pairs):
    """
    Prints murder-target pairs into seperate text files for easy copying.
    :param pairs: A dictionary of murder-target pairs.
    """
    with open('murderers.txt', 'w') as murderer_file:
        with open('targets.txt', 'w') as targets_file:
            for key in pairs.keys():
                murderer_file.write("%s\n" % key)
                targets_file.write("%s\n" % pairs[key])



names_list = read_names_from_file(args.names)
murder_pairs = create_cycle(names_list)
print_pairs(murder_pairs)
save_pairs(murder_pairs)
save_pairs_seperated(murder_pairs)
