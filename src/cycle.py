#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('names',
                    type=argparse.FileType('r'),
                    help='Path to a file containing names for creating a circle of "murderer-murdered" pairs.'
                         'Only one name per line is allowed. Names may contain spaces.')

args = parser.parse_args()