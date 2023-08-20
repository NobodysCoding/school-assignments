def isSorted(lst):
    if len(lst) < 2:
        return True
    
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    
    return True

# Test cases
print(isSorted([]))             # True
print(isSorted([1]))            # True
print(isSorted([1, 2, 3, 4]))   # True
print(isSorted([4, 3, 2, 1]))   # False
print(isSorted([1, 3, 2, 4]))   # False
