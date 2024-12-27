'''The goal is to load the text from 'https://adventofcode.com/2023/day/1/input' and find the 'calibration value' from each line, 
then sum all calibration values. The calibration value is found from the first and last digit in each string.
e.g. abgfb1hfoa5ahfos7 has calibration value 17.
'''

#data is saved locally in 01.txt
data = open('./2023/01.txt').read().split()
# print(data)

total_count = 0
number_count = 0

#retrieve the first number in a string
def findFirstValue(word):
  for letter in word:
    if(letter.isnumeric()):
      return int(letter)
    
def findLastValue(word):
  for letter in word[::-1]: #same as findFirstValue, but on the reverse of the word
    if(letter.isnumeric()):
      return int(letter)
    
for line in data:
  # print(line)
  # print("--------------------------")
  number_count += 10*findFirstValue(line) + findLastValue(line)


print(f'Count referring only to digits: {number_count}')

numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

def findFirstWord(word):
  #create a temporary substring. We will append letters from the word one at a time to the substring
  temp = ""
  for i in range (0, len(word)+1):
    temp = temp + word[i] #append
    #check if any number word is in the substring. If so, add that number into the word at the correct index
    for num in numbers.keys():
      if num in temp:
        return numbers[num]
      
def findLastWord(word):
  #create a temporary substring. We will append letters from the word one at a time to the substring
  temp = ""
  for i in range (0, len(word)):
    temp = word[-1-i] + temp #append
    #check if any number word is in the substring. If so, add that number into the word at the correct index
    for num in numbers.keys():
      if num in temp:
        return numbers[num]
      
number_count = 0

for line in data:
  number_count += 10*findFirstWord(line) + findLastWord(line)

print(f'Count referring to digits and words: {number_count}')

# example = "two1nine eightwothree abcone2threexyz xtwone3four 4nineeightseven2 zoneight234 7pqrstsixteen"

# for i in example.split():
#   count = findFirstWord(i)*10 + findLastWord(i)
#   print(f'word: {i}, count: {count}')