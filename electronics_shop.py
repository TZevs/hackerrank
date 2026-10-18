def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()

    # Pointers for moving through the arrays.
    # Starting at the cheapest drive
    j = 0 
    # Starting at the most expensive keyboard
    i = len(keyboards) - 1 
    best = -1

    # Loop while i and j are within their array indexes.
    while i >= 0 and j < len(drives):
        total = keyboards[i] + drives[j]

        if total <= b:
            best = max(best, total)
            # try a more expensive drive
            j += 1
        else:
            # went over budget, try a cheaper keyboard
            i -= 1

    return best

print(getMoneySpent([3,1], [5,2,8], 10))