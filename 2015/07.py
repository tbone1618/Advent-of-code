import numpy as np

with open('./2015/07.txt') as f:
    data = [line.rstrip('\n') for line in f]

# Unsigned ints can be created using numpy's np.uint16({num})

def partOne():
    
    # This dictionary will be (node: value) pairs for easy lookup
    # e.g. 
    # a: 15
    # b: 25
    signals = {}

    # This dictionary will be (node: operation) pairs for easy lookup
    # e.g.
    # ls : lf AND lq
    # jn: iu RSHIFT 1
    operations = {}

    for line in data:
        line = line.split("->")
        operations[line[1].strip()] = line[0].split()
        # print(line)

    print(operations)

  # Operations to define:
    # NOT: bitwise complement
    # AND: bitwise and
    # OR: bitwise or
    # LSHIFT: bitwise leftshift
    # RSHIFT: bitwise rightshift

    # We need to find all operations that lead into node `a`. Recursion will be our best bet here.
    def calculateNode(node):
        # First case: simple assignment of x -> y
        if len(operations[node]) == 1:
            #recursion step
            if operations[node][0] not in signals:
                calculateNode(operations[node][0])

            signals[node] = operations[node]

        # Unary case: NOT x -> y
        elif operations[node][0] == "NOT":
            #recursion step
            if operations[node][1] not in signals:
                calculateNode(operations[node][1])

            signals[node] = ~operations[node][1]
          
        # All other cases: x OPERATION z -> y
        else:
          first = operations[node][0]
          second = operations[node][2]
          operation = operations[node][1]

          #recursion step
          for child in (first, second):
              if child not in signals:
                  calculateNode(child)
        
          if operation == "AND":
              signals[node] = first & second
          elif operation == "OR":
              signals[node] = first | second
          elif operation == "LSHIFT":
              signals[node] = first << second
          elif operation == "RSHIFT":
              signals[node] = first >> second
          
    # calculateNode("a") 
    print(f'Operations for `a`: {operations["a"]}')       

    calculateNode("a")

partOne()