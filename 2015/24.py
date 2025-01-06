with open('./2015/24.txt') as f:
    data = [int(line.rstrip('\n')) for line in f]

# The weight that each group needs to be
# 3 groups of equal weight in total
weight = int(sum(data)/3)


