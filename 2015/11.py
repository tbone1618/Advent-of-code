def checkPassword(word: str):
  """A method that checks the if the password meets the required conditions with regex.

  Args:
      word (str): The password being checked

  Returns:
      bool: Truth value for whether the password is valid
  """


  return False


# It is easier to change elements when the input is a list, because strings are immutable
# Might need to make it a string for the regex part
def incrementPassword(word: list, position: int):
  """Increments the password at the letting in position `position`

  Args:
      word (str): The password to be incremented
      position (int): The position where the password is incremented

  Returns:
      str: The updated password after incrementing
      position: The next position to be incremented
  """

  # minimum value a = 97
  # maximum value z = 122
  # skip values for i, o, l are 105, 111, and 108
  charOrd = ord(word[position])

  # If the character is `z`, change it to `a` and increment next letter
  if charOrd == 122:
    word[position] = "a"
    word, position = incrementPassword(word, position - 1)
  # If the character is `h`, `k`, or `n` then it needs to be incremented twice to skip `i`, `l`, or `o` respectively
  elif charOrd == 104 or charOrd == 110 or charOrd == 107:
    word[position] = chr(charOrd + 2)
  else:
    word[position] = chr(charOrd+1)

  return word, position


def partOne():

  password = "cqjxjnds"
  index = len(password) - 1

  # Run a while loop that checks the password, and if the password is invalid increment it
  while not checkPassword(password):
    password = incrementPassword

  print(password)

password = list("cqjxjnds")
index = len(password) - 1



