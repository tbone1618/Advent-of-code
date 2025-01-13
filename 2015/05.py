import re
# An exercise in regex

with open('./2015/05.txt') as f:
    data = [line.rstrip('\n') for line in f]

'''
    1. It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    2. It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    3. It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
'''

def exploration():
  example = "ugknbfddgicrmopn"

  # 1: Check string for at least 3 vowels
  # using a set [] searches for any instances of a character in that set
  match = re.findall(r'[aeiou]', example)
  num_found = len(match)
  print('Check 1: looking for 3 or more vowels')
  print(f'vowel matches: {match}')
  print(f'number of vowels: {num_found}')

  # 2. Check string for letter twice in a row
  # (.) captures any character. 
  # \1 references that character, and 
  # {1,} checks for 1 or more occurrences of the captured character following that character
  match = re.search(r'(.)\1{1,}', example)
  print('Part 2: checking for a double occurrence of a letter')
  print(match)

  # 3. Check string for instances of substrings
  naughty_strings = ["ab", "cd", "pq", "xy"]
  print("Check 3: checking for naughty strings")
  print(re.findall(r"(?=("+'|'.join(naughty_strings)+r"))", example))

#Putting it all together
def partOne():
  total_nice_strings = 0
  naughty_strings = ["ab", "cd", "pq", "xy"]

  print("Part One: Counting the nice words in Santa's List")

  for word in data:
    # print()
    # print("Word to check:")
    # print(word)
    match = re.findall(r'[aeiou]', word)
    num_found = len(match)
    if num_found > 2:
      # print("passed first check")
      match = re.search(r'(.)\1{1,}', word)
      if match:
        # print("passed second check")
        if not any(naughty in word for naughty in naughty_strings):
          # print("passed third check")
          total_nice_strings = total_nice_strings + 1

  print(f'Total nice strings in list: {total_nice_strings}')
  print()



def partTwo():

  total_nice_strings = 0

  #   a nice string is one with all of the following properties:

  #   It contains a pair of any two letters that appears at least twice in the string without overlapping, 
  #   like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).

  #   It contains at least one letter which repeats with exactly one letter between them, 
  #   like xyx, abcdefeghi (efe), or even aaa.

  pattern1 = r"(..).*\1" #Search for a consecutive pair of two letters (like "xyxy")
  pattern2 = r"(.).\1" #Search for 4 letters in a row (like "aaaa")


  for word in data:
    match1 = re.search(pattern1, word)
    if match1:
      match2 = re.search(pattern2, word)
      if match2:
        total_nice_strings = total_nice_strings + 1

  print(total_nice_strings)

# exploration()
# partOne()
partTwo()