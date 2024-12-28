import re
# An exercise in regex

file = open("./2015/05.txt")
data = file.read()
file.close()

example = "ugknbfddgicrmopn"

'''
    1. It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    2. It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    3. It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
'''

# 1: Check string for at least 3 vowels
# using a set [] searches for any instances of a character in that set
match = re.findall(r'[aeiou]', example)
num_found = len(match)
print(f'vowel matches: {match}')
print(f'number of vowels: {num_found}')