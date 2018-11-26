# Crow Cycle
A small script for generating "murderer-murdered" pairs for the so called assassin's game (see 
[http://www.games-wiki.org/wiki/Assassin_game/](http://www.games-wiki.org/wiki/Assassin_game/)).

# How does it work?
The script takes a list of the participants' names as input.
See [names.txt](names.txt) for an example of such a list of names.
The script shuffles the names and puts them into a list.
This shuffled list is then interpreted as the cycle of murderers and persons to be murdered,
i.e. the (x)-th person has to kill the (x+1)-th person (Note: the last person has to kill the first person again).
The output is shuffled again in order to avoid leaking information.

# Usage
```
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
                        Path to the output file. If not specified, the output
                        is written to the standard output.
```
