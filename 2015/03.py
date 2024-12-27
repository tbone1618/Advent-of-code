data = open("./2015/03.txt").read()

def partOne():
  x = 0
  y = 0
  house_tracker = {"0, 0": 1}

  # print(data)
  # test = f'{x} + {y}'
  # print(test)

  def addPresent(x, y):
    if f'{x}, {y}' in house_tracker:
      house_tracker[f'{x}, {y}'] += 1
    else:
      house_tracker[f'{x}, {y}'] = 1


  for letter in data:
    if letter == '^':
      y += 1
    elif letter == 'v':
      y -= 1
    elif letter == '>':
      x += 1
    elif letter == '<':
      x -= 1
    
    addPresent(x,y)

  print("Houses visited in part one:")
  print(len(house_tracker))
  # print(house_tracker)

def partTwo():
  x1, x2, y1, y2 = 0, 0, 0, 0

  house_tracker = {"0, 0": 1}

    # print(data)
    # test = f'{x} + {y}'
    # print(test)

  def addPresent(x, y):
    if f'{x}, {y}' in house_tracker:
      house_tracker[f'{x}, {y}'] += 1
    else:
      house_tracker[f'{x}, {y}'] = 1

  santa_path = data[::2]
  robot_path = data[1::2]

  print(santa_path)
  print(robot_path)

  for letter in santa_path:
    if letter == '^':
      y1 += 1
    elif letter == 'v':
      y1 -= 1
    elif letter == '>':
      x1 += 1
    elif letter == '<':
      x1 -= 1
  
    addPresent(x1, y1)

  for letter in robot_path:
    if letter == '^':
      y2 += 1
    elif letter == 'v':
      y2 -= 1
    elif letter == '>':
      x2 += 1
    elif letter == '<':
      x2 -= 1
  
    addPresent(x2, y2)

  print("Houses visited in part two:")
  print(len(house_tracker))


partOne()
partTwo()
