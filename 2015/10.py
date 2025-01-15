number = "3113322113"

def lookSay(num: str):
  tempString = num
  length = len(tempString)

  digit = tempString[0]
  count = 1
  newNum = ""

  # Walk down the string to get counts of each digit
  for i in range(1, length):
    if tempString[i] != digit:
      newNum = newNum + str(count) + digit
      digit = tempString[i]
      count = 1
    else:
      count = count + 1

  newNum = newNum + str(count) + digit

  return(newNum)

# print(lookSay(number))

for i in range(0, 40):
  number = lookSay(number)

print(len(number))