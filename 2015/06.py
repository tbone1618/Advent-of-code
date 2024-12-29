import numpy as np

# with open('./2015/06.txt') as f:
#     data = [line.rstrip('\n') for line in f]

# eventually we will work with a 1000x1000 array, but for now do 10x10
example_lights = np.zeros((10,10), dtype=bool)
print(example_lights)

# Example inputs to test the methods on
example_on = "turn on 0,9 through 0,9"
example_off = "turn off 2,7 through 0,9"
example_toggle = "toggle 0,9 through 2,7"

def switchOnLights():
  """
  Turns on all lights in the square (x1, y1) through (x2, y2)
  args: will probably take in lightArray, firstCoords, secondCoords.
    I am not sure if I want to pass in x and y individually, or as tuples
  
  No return, alter lightArray in place.
  """
  return

def switchOffLights():
  """
  Operates similar to switch on, but will turn lights off instead.
  """
  return

def toggleLights():
  """
  will invert the lights in the inputted square
  """
