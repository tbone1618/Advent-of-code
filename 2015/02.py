data = open('./2015/02.txt').read().split('\n')

def boxArea(x, y, z):
  a1 = x*y
  a2 = x*z
  a3 = y*z

  total = 2*(a1 + a2 + a3) + min(a1, a2, a3)

  return total

def ribbonLength(x, y, z):
  length = 2*(x + y + z) - 2*max(x,y,z) + x*y*z
  return length


def partOne():
  total_paper = 0
  side1 = 0
  side2 = 0
  side3 = 0

  for line in data:
    # print(line)
    split_line = line.split('x')
    side1 = int(split_line[0])
    side2 = int(split_line[1])
    side3 = int(split_line[2])

    total_paper = total_paper + boxArea(side1, side2, side3)

  print(total_paper)

def partTwo():
  total_ribbon = 0
  side1 = 0
  side2 = 0
  side3 = 0

  for line in data:
    split_line = line.split('x')
    side1 = int(split_line[0])
    side2 = int(split_line[1])
    side3 = int(split_line[2])

    total_ribbon = total_ribbon + ribbonLength(side1, side2, side3)

  print(total_ribbon)


partOne()
partTwo()
