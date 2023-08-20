def printAll(seq):
    if not seq:
        return
    print(seq[0])
    printAll(seq[1:])

# Testing the function
sequence = [1, 2, 3, 4, 5]
printAll(sequence)
