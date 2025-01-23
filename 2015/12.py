import json

with open('./2015/12.json', 'r') as file:
    data = json.load(file)

def countNumbers(data):

  if isinstance(data, int):
     return data

  if isinstance(data, str):
     return 0 
  
  if isinstance(data, list):
     return sum(countNumbers(item) for item in data)
  
  if isinstance(data, dict):
     for value in data.values():
        if value == "red":
           return 0
     return sum(countNumbers(value) for value in data.values())
  
  return 0

print(countNumbers(data))