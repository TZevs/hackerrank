# Works for the smaller values, but the constraint has n & m up to 10^9
def bruteSaveThePrisoner(n, m, s):
    position = s
    counter = 1
    while counter != m:
        print("Pos:", position)
        print("Counter:", counter)
        if position > n:
            position = 1
        position += 1 
        counter += 1

    return position

def fuckedSaveThePrisoner(n, m, s):
    numOfLoops = round(m / n)

    startingRange = list(range(s, n+1))
    originalRange = list(range(1, n+1))

    if m <= len(startingRange):
        return startingRange[m-1]

    if s == 1:
        fullLoops = numOfLoops * n
        leftOver = m - fullLoops
        return originalRange[leftOver-1]

    exceptEnd = len(startingRange) + len(originalRange) * (numOfLoops - 1)
    diff = m - exceptEnd
    print(originalRange)
    return originalRange[diff-1]

def saveThePrisoner(n, m, s):
    # Converts the starting position to 0-indexed, 
    # adds the number of sweets to be distributed (with consideration for 0-indexing),  
    # then gets remainder, after completing full loops of the prisoners, to find the final position.
    # Finally, it converts back to 1-indexed by adding 1.

    return (s - 1 + m - 1) % n + 1

print(saveThePrisoner(3, 6, 1)) 
print("===")
print(saveThePrisoner(7, 31, 1)) 
print("===")
print(saveThePrisoner(3, 8, 4)) 