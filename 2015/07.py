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

        # A typical line looks like "gz LSHIFT 15 -> hd"

        # Key: the part after "->"
        key = line[1].strip()

        # Value: the part before "->". If any part of this is numeric, we want to convert it to an
        # unsigned int now to make calculations during the recursive step easier
        value = [int(part) if part.strip().isnumeric() else part.strip() for part in line[0].split()]

        operations[key] = value

    print(operations)

  # Operations to define:
    # NOT: bitwise complement
    # AND: bitwise and
    # OR: bitwise or
    # LSHIFT: bitwise leftshift
    # RSHIFT: bitwise rightshift

    # We need to find all operations that lead into node `a`. Recursion will be our best bet here.
    def calculateNode(node):
        print(f'Calculating node {node}:')

        # First case: simple assignment of x -> y
        if len(operations[node]) == 1:
            child = operations[node][0]
            # child is a node (str) or an int
            if isinstance(child, str):
                if child not in signals:
                    calculateNode(child)
                    signals[node] = signals[child] & 0xFFFF # use 0xFFFF to mask the int and bound it between 0 and 65535
            # child is a number
            else:
                signals[node] = child & 0xFFFF


        # Unary case: NOT x -> y
        elif operations[node][0] == "NOT":
            child = operations[node][1]
            # child is a string, e.g. a node
            if isinstance(child, str):
                if child not in signals:
                    calculateNode(child)
                    signals[node] = ~signals[child] & 0xFFFF
            # child is a number
            else:
                signals[node] = ~child & 0xFFFF
          
        # All other cases: x OPERATION z -> y
        else:
            first = operations[node][0]
            second = operations[node][2]
            operation = operations[node][1]

            # if first or second are strings, we need to retrieve their value from signals
            # Otherwise first or second is an int and we don't have to reassign
            if isinstance(first, str):
                if first not in signals:
                    calculateNode(first)
                first = signals[first]

            if isinstance(second, str):
                if second not in signals:
                    calculateNode(second)
                second = signals[second]


            if operation == "AND":
                signals[node] = (first & second) & 0xFFFF
            elif operation == "OR":
                signals[node] = (first | second) & 0xFFFF
            elif operation == "LSHIFT":
                signals[node] = (first << second) & 0xFFFF
            elif operation == "RSHIFT":
                signals[node] = (first >> second) & 0xFFFF

        print(f'Signal at {node}: {signals[node]}')

    calculateNode("a")

partOne()