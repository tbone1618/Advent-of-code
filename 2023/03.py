'''Thoughts: Rather than searching for numbers that are next to symbols, I think 
it might be easier to check if the ALL of the symbols around each number are dots.
This way we don't have to figure out how long each number next to a symbol is.
If at least one character around a number is not a dot or a number, then it must be
next to a symbol, and we can add it to the sum.
This also aims to avoid handling overcounting numbers that have multiple symbols around them.
'''

import re

data = open('./03.txt').read().split("\n")

def partOne():
  
  pass