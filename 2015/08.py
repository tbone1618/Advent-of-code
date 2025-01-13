with open('./2015/08.txt') as f:
  data = [line.rstrip('\n') for line in f]
  # processedData = [line.rstrip('\n').encode('utf-8').decode('unicode_escape') for line in f]

with open('./2015/08.txt') as f:
  processedData = [line.rstrip('\n').encode('utf-8').decode('unicode_escape') for line in f]

totalChars = 0
stringChars = 0
encodeChars = 0

quoteCount = 0
slashCount = 0

# The result from the below code is too low currently

for line in data:
    # print(line)
    totalChars = totalChars + len(line)

    quoteCount = line.count("\"")
    slashCount = line.count("\\")

    #Every " and \ adds 1 additional character
    encodeChars = encodeChars + len(line) + quoteCount + slashCount + 2


print(f'Total Characters: {totalChars}')

for line in processedData:
    # print(line)
    stringChars = stringChars + len(line) - 2 #subtract 2 because quotation marks on each end don't count

print(f'String Characters: {stringChars}')

print(f'Encode Characters: {encodeChars}')

print(f'Difference: {totalChars - stringChars}')

print(f'Part 2: {encodeChars - totalChars}')