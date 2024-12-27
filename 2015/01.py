import os

data = open('./2015/01.txt').read()

# print(data)

floor = 0
place = 1

for letter in data:
  if letter == "(":
    floor = floor + 1
  elif letter == ")":
    floor = floor - 1

  if floor == -1:
    print(f'the basement was entered at place {place}')
  place = place + 1

print(floor)