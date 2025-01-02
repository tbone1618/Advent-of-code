import numpy as np

# with open('./2015/06.txt') as f:
#     data = [line.rstrip('\n') for line in f]

# TODO rewrite the light array to be a class, and the functions as object methods

# eventually we will work with a 1000x1000 array, but for now do 10x10
example_lights = np.zeros((10,10), dtype=bool)
# print(example_lights)

# Example inputs to test the methods on
example_on = "turn on 0,9 through 0,9"
example_off = "turn off 2,7 through 0,9"
example_toggle = "toggle 0,9 through 2,7"

def parseInput(stringToParse: str) -> list:
  operation = ""
  parsedList = []

  split = stringToParse.split()
  if split[0] == "toggle":
    operation = "toggle"
    firstCoordinates = split[1].split(",")
    secondCoordinates = split[3].split(",")
  elif split[1] == "on":
    operation == "on"
    firstCoordinates = split[2].split(",")
    secondCoordinates = split[4].split(",")
  elif split[1] == "off":
    operation = "off"
    firstCoordinates = split[2].split(",")
    secondCoordinates = split[4].split(",")
  else:
    print("Invalid string to parse")
    operation = "invalid"

  parsedList.append(operation)
  parsedList.extend(firstCoordinates)
  parsedList.extend(secondCoordinates)

  return(parsedList)


def switchOnLights(x1: int, y1: int, x2: int, y2:int, lightArray: list[list[bool]]):
  """
  Turns on all lights in the square (x1, y1) through (x2, y2)
  args: ...
  """

  for i in range (x1, x2+1):
    for j in range (y1, y2+1):
      lightArray[i][j] = True

def switchOffLights(x1: int, y1: int, x2: int, y2:int, lightArray: list[list[bool]]):
  """
  Operates similar to switch on, but will turn lights off instead.
  """
  for i in range (x1, x2+1):
    for j in range (y1, y2+1):
      lightArray[i][j] = False

def toggleLights(x1: int, y1: int, x2: int, y2:int, lightArray: list[list[bool]]):
  """
  will invert the lights in the inputted square
  """
  for i in range (x1, x2+1):
    for j in range (y1, y2+1):
      lightArray[i][j] = not lightArray[i][j]

switchOnLights(2, 2, 4, 4, example_lights)
print(example_lights)
switchOffLights(2, 2, 3, 3, example_lights)
print(example_lights)
toggleLights(2, 2, 4, 4, example_lights)
print(example_lights)

print(parseInput(example_toggle))