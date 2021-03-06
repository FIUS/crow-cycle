#!/usr/bin/env python3

import argparse
import json
import os
import sys

# If you change the arguments, please update the usage section in README.md
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input',
                    type=argparse.FileType('r'),
                    help='Path to the json file generated by cycle.py. '
                         'If not specified, the input is read from the standard input.')
parser.add_argument('-o', '--output',
                    type=argparse.FileType('w'),
                    help='Path to the output file. Output is tex. '
                         'If not specified, the output is written to the standard output.')
parser.add_argument('--desc',
                    default='',
                    help='Description that is printed in every table row.')
args = parser.parse_args()


def read_from_input(file):
    if file is None:
        file = sys.stdin
    return file.read()


def create_tex(desc, pairs):
    table_lines = ["{} & {} & {}".format(desc, first, second)
                   for first, second in pairs]
    table_content = '\n\\\\\\hline\n'.join(table_lines)
    with open(os.path.join(os.path.dirname(__file__), 'template.tex'), 'r') as template:
        tex_template = template.read()
    return tex_template.replace('NAMES', table_content)


def write_to_output(file, str):
    if file is None:
        file = sys.stdout
    file.write(str)


murder_pairs = json.loads(read_from_input(args.input))
murder_tex = create_tex(args.desc, murder_pairs)
write_to_output(args.output, murder_tex)
