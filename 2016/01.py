# remove all the white space, split by ','
data = open("./2016/01.txt").read().replace(" ", "").split(',')

def partOne():
  x = 0
  y = 0
  orientation = 0
  distance_to_move = 0

  for instruction in data:

    # Setting the orientation
    if instruction[0] == "R":
      orientation += 1
    elif instruction[0] ==  "L":
      orientation -= 1
    orientation = orientation % 4

    # moving in the direction
    distance_to_move = int(instruction[1:])

    # North
    if orientation == 0:
      y += distance_to_move

    # East
    elif orientation == 1:
      x += distance_to_move
    
    # South
    elif orientation == 2:
      y -= distance_to_move

    # West
    elif orientation == 3:
      x -= distance_to_move

  print(f'Total blocks away: {abs(x) + abs(y)}')
    
# partOne()
