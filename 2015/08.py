with open('./2015/08.txt') as f:
  data = [line.rstrip('\n') for line in f]
  # processedData = [line.rstrip('\n').encode('utf-8').decode('unicode_escape') for line in f]

with open('./2015/08.txt') as f:
  processedData = [line.rstrip('\n').encode('utf-8').decode('unicode_escape') for line in f]

totalChars = 0
stringChars = 0

# The result from the below code is too low currently

for line in data:
    # print(line)
    totalChars = totalChars + len(line)

print(f'Total Characters: {totalChars}')

print("**************************************************************************")

for line in processedData:
    # print(line)
    stringChars = stringChars + len(line) - 2 #subtract 2 because quotation marks don't count

print(f'String Characters: {stringChars}')

print(f'Difference: {totalChars - stringChars}')