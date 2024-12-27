'''The Elf would first like to know which games would have been possible if
the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes
'''

data = open('./2023/02.txt').read().split("\n")


def partOne():
  game_id = 0
  total = 0
  # round_id = 0
  colors = {'red': 12, 'green': 13, 'blue': 14}
  count_game = True

  for line in data:
    #track game_id
    game_id = game_id + 1
    count_game = True
    # round_id = 0

    #only need information after the colon
    line = line.split(":")[1]
    # print(f'game: {game_id}')
    # print(line)

    #each round is separated by a semi-colon
    for round in line.split(";"):
      # round_id = round_id + 1
      # print(f'round: {round_id}')
      # print(round)

      #each color count is separated by a comma
      for color in round.split(","):
        i = color.split()
        #if a color was counted more times then possible, do not count the game
        if int(i[0]) > colors[(i[1])]:
          count_game = False
        # print(color)

    if(count_game):
      total = total + game_id

  print(total)

#part 1 complete

def partTwo():

  total = 0

  #track the min number of each cube
  colors = {"red": -1, "green": -1, "blue": -1}
  power_total = 1

  for line in data:
    #reset min colors data and power_total at the start of each game
    colors = {"red": -1, "green": -1, "blue": -1}
    power_total = 1

    #only need information after the colon
    line = line.split(":")[1]

    #each round is separated by a semi-colon
    for round in line.split(";"):

      #each color count is separated by a comma
      for color in round.split(","):
        
        i = color.split()
        #compare the number of cubes in the game to the min number of cubes
        if int(i[0]) > colors[(i[1])]:
          colors[(i[1])] = int(i[0])
  #after the minimums have been established for this game, find the power
  #and add it to the total
    print(colors)
    for i in colors:
      power_total = power_total*colors[i]

    total = total + power_total

  print(total)

# partOne()
partTwo()