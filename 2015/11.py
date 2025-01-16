def checkPassword(word: str):
  """A method that checks the if the password meets the required conditions with regex.

  Args:
      word (str): The password being checked

  Returns:
      bool: Truth value for whether the password is valid
  """


  return False

def incrementPassword(word: str, position: int):
  """Increments the password at the letting in position `position`

  Args:
      word (str): The password to be incremented
      position (int): The position where the password is incremented

  Returns:
      str: The updated password after incrementing
  """

  return word


def partOne():

  password = "cqjxjnds"
  index = len(password) - 1

  # Run a while loop that checks the password, and if the password is invalid increment it
  while not checkPassword(password):
    password = incrementPassword

  print(password)

password = "cqjxjnds"
index = len(password) - 1
print(password[index])
print(ord(password[index]))
print(chr(ord(password[index])+1))

ord(password[index])
