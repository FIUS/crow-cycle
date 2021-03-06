# crow-cycle

A small script for generating "murderer-murdered" pairs for the so called assassin's game (see 
[http://www.games-wiki.org/wiki/Assassin_game/](http://www.games-wiki.org/wiki/Assassin_game/)).

## How does it work?

Every participant is assigned a random other participant he has to "murder".
This is done in such a way that a single cycle is generated among
the participants.
I.e. when following the murderer-victim relations,
one visits every participant before reaching the first one again.
The output of the cycle generation is shuffled as well which prevents
any information leakage.

## Usage

The main script is `crow-cycle.py`.
It takes a list of the participants' names as input and creates a PDF containing the output.
[names.txt](names.txt) contains an example input, so the usual workflow would be:

* Clone this repo.
* Put your participants' names into [names.txt](names.txt).
* Run `./crow-cycle.py -i names.txt --desc 'Game 1' -o crow-cycle.pdf`.

Alternatively to writing the resulting PDF to *crow-cycle.pdf*, you can write it to *stdout*, for example in order to print it:

```bash
./crow-cycle.py -i names.txt --desc 'Game 1' | lpr
```

### Details for `./crow-cycle.py`

```txt
usage: crow-cycle.py [-h] [-i INPUT] [-o OUTPUT] [--desc DESC]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to the file containing names for creating a
                        circle of "murderer-murdered" pairs. Only one name per
                        line is allowed. Names may contain spaces. If not
                        specified, the input is read from the standard input.
  -o OUTPUT, --output OUTPUT
                        Path to the output file. Output is pdf. If not
                        specified, the output is written to the standard
                        output.
  --desc DESC           Description that is printed in every table row.
```

## Technical Details

Internally, `crow-cycle.py` uses three other programs:

* `src/cycle.py` outputs the cycle as JSON
* `src/tex.py` creates a LaTeX source from that JSON
* `latexmk` is used in order to compile that LaTeX source to PDF

### Details for `src/cycle.py`

```txt
usage: cycle.py [-h] [-i INPUT] [-o OUTPUT]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to the file containing names for creating a
                        circle of "murderer-murdered" pairs. Only one name per
                        line is allowed. Names may contain spaces. If not
                        specified, the input is read from the standard input.
  -o OUTPUT, --output OUTPUT
                        Path to the output file. Output is json. If not
                        specified, the output is written to the standard
                        output.
```

### Details for `src/tex.py`

```txt
usage: tex.py [-h] [-i INPUT] [-o OUTPUT] [--desc DESC]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to the json file generated by cycle.py. If not
                        specified, the input is read from the standard input.
  -o OUTPUT, --output OUTPUT
                        Path to the output file. Output is tex. If not
                        specified, the output is written to the standard
                        output.
  --desc DESC           Description that is printed in every table row.
```
