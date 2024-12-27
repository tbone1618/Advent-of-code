import hashlib

def partOne():
  data = "bgvyzdsv"

  # We need to search for a has with 5 leading zeros.
  # We will break the loop once a hash is found
  hash_found = False
  i = 0
  temp_string = ""

  while(not hash_found):
    temp_string = data + str(i)

    
    #encode, update, find hash
    data_bytes = str.encode(temp_string)
    h = hashlib.md5(data_bytes)
    temp_hash = h.hexdigest()

    # Break the loop if the first 5 characters are 0

    # print()
    # print(i)
    # print(f"Temp String: {temp_string}")
    # print(f"Temp hash: {temp_hash}")
    # print(f"First 5: {temp_hash[0:5]}")

    if(temp_hash[0:5] == "00000"):
      hash_found = True

    i += 1

  print("Lowest hash: ")
  print(temp_string)



def partTwo():
    data = "bgvyzdsv"

    # We need to search for a has with 5 leading zeros.
    # We will break the loop once a hash is found
    hash_found = False
    i = 0
    temp_string = ""

    while(not hash_found):
      temp_string = data + str(i)

      
      #encode, update, find hash
      data_bytes = str.encode(temp_string)
      h = hashlib.md5(data_bytes)
      temp_hash = h.hexdigest()

      # Break the loop if the first 5 characters are 0

      # print()
      # print(i)
      # print(f"Temp String: {temp_string}")
      # print(f"Temp hash: {temp_hash}")

      if(temp_hash[0:6] == "000000"):
        hash_found = True

      i += 1

    print("Lowest hash: ")
    print(temp_string)

# partOne()
partTwo()