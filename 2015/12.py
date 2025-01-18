import json

with open('./2015/12.json', 'r') as file:
    data = json.load(file)

def countNumbers(data):
  
  sum = 0

  for item in data:
      # Types to consider:
      # Dictionary {}
      # List []
      # String ""
      # Int 0

      # Can use the map() function on iterablews

      if type(item) == type({}):
         # TODO 
         pass
      
      if type(item) == type([]):
         # TODO
         pass
      
      if type(item) == type(""):
         return 0
      
      if type(item) == type(0):
         return item
         
      pass
          
  return sum

print(countNumbers(data))