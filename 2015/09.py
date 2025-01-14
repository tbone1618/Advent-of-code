import numpy as np

# loading the data
with open('./2015/09.txt') as f:
  data = [line.rstrip('\n') for line in f]

# The distance between cities can be represented as an array, where the ith and jth row is the distance between ith and jth cities.
# It will have zeros on the diagonal, and we will never make a comparison where i = j
routes = np.full((8,8), 0, dtype=int)

i = 0   #row
j = 1   #column
# cityIndex = 0
# cities = {}

for line in data:
  #Loading the routes into an arry
  routes[i][j] = int(line.split()[4])
  routes[j][i] = int(line.split()[4])
  j = j + 1
  if j > 7:
    i = i + 1
    j = i + 1
  
  # # Loading cities into a dictionary
  # for city in (line.split()[0], line.split()[2]):
  #   if city not in cities:
  #     cities[city] = cityIndex
  #     cityIndex = cityIndex + 1

#TODO find the best route with each city as the starting city
# Find the largest distance city pair
maxIndex =  np.unravel_index(np.argmax(routes), routes.shape)
# Make one of those cities our starting city
currentCity = maxIndex[1]

# Replace zeros with large numbers so that we can find minimums without grabbing zeros
routes = np.where(routes == 0, 9999, routes)

print(routes)

totalDistance = 0

def findClosestCity(currentCity: int):
  #Find the closest city to current city, add that distance to totalDistance
  nextCity = np.argmin(routes[currentCity])
  totalDistance = totalDistance + routes[currentCity][nextCity]

  return nextCity

i = 0
while i < 7:

  nextCity = np.argmin(routes[currentCity])
  # print(f'current city: {currentCity}')
  # print(f'next city: {nextCity}')
  print(f'distance traveled this hop: {routes[currentCity][nextCity]}')
  totalDistance = totalDistance + routes[currentCity][nextCity]
  routes[currentCity, :] = 9999
  routes[:, currentCity] = 9999
  currentCity = nextCity
  print(f'this is iteration number {i}')
  print(f'total distance traveled so far: {totalDistance}')
  # print(routes)
  i = i + 1

print(totalDistance)

  

