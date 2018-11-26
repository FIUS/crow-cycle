# Crow Cycle
A small script for generating "murderer-murdered" pairs for the so called assassin's game (see 
[http://www.games-wiki.org/wiki/Assassin_game/](http://www.games-wiki.org/wiki/Assassin_game/)).

# How does it work?
The script takes a path to a text file containing the names of all participants as first parameter.
See [names.txt](names.txt) for an example of such a list of names.
The script shuffles the names and puts them into a list. 
This shuffled list is then interpreted as the cycle of murderers and persons to be murdered,
i.e. the (x)-th person has to kill the (x+1)-th person (Note: the last person has to kill the first person again).
