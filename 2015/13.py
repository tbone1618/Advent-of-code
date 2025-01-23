import numpy as np

with open('./2015/13.txt') as f:
  data = [line.rstrip('\n') for line in f]

# This problem will flow similar to day 9, but the array will not be symmetric.

seats = np.full((8,8), 0, dtype=int)

i = 0 # Row index
j = 1 # Column index
sign = 1

# Line example
# "Alice would gain 54 happiness units by sitting next to Bob."

# Loading the data into the array
for line in data:
  line = line.split()

  # Check if this is a positive or negative point change
  if line[2] == "gain":
    sign = 1
  else:
    sign = -1

  seats[i][j] = int(line[3]) * sign

  # Move forward one column index. Skip where j == i because a person cannot sit next to their self.
  
  j += 1
  if j == i:
    j += 1
  elif j > 7:
    i = i + 1
    j = 0

print(seats)
