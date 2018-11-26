#!/usr/bin/env python3

import argparse
import os
import shutil
import subprocess
import sys

# If you change the arguments, please update the usage section in README.md
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input',
                    help='Path to the file containing names for creating a circle of "murderer-murdered" pairs. '
                         'Only one name per line is allowed. Names may contain spaces. '
                         'If not specified, the input is read from the standard input.')
parser.add_argument('-o', '--output',
                    help='Path to the output file. Output is pdf. '
                         'If not specified, the output is written to the standard output.')
parser.add_argument('--desc',
                    help='Description that is printed in every table row.')
args = parser.parse_args()

# mkdir -p build
if not os.path.exists('build'):
    os.mkdir('build')

# src/cycle.py -i <input> | src/tex.py -o build/crow-cycle.tex
cycle_cmd = ['src/cycle.py']
if args.input is not None:
    cycle_cmd += ['-i', args.input]
tex_cmd = ['src/tex.py', '-o', 'build/crow-cycle.tex']
if args.desc is not None:
    tex_cmd += ['--desc', args.desc]
cycle_pipe = subprocess.Popen(cycle_cmd, stdout=subprocess.PIPE)
subprocess.run(tex_cmd, stdin=cycle_pipe.stdout, stdout=sys.stderr)
cycle_pipe.wait()

# cd build; latexmk --pdf crow-cycle.tex; cd ..
subprocess.run(['latexmk', '--pdf', 'crow-cycle.tex'], cwd='build', stdout=sys.stderr)

if args.output is None:
    # cat build/crow-cycle.pdf
    with open('build/crow-cycle.pdf', 'rb') as pdf:
        sys.stdout.buffer.write(pdf.read())
else:
    # mv build/crow-cycle.pdf <output>
    os.rename('build/crow-cycle.pdf', args.output)

# rm -rf build
shutil.rmtree('build')
