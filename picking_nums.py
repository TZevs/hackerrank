# Definitly the wrong solution, could possible work but far to complicated.
def pickingNumbers(a):
    a.sort()
    print(a)
    count = []
    vals = []
    print(len(a))

    for i in range(len(a) - 1):
        if abs(a[i] - a[i+1]) <= 1:
            print(f"{a[i]} - {a[i+1]} = {abs(a[i] - a[i+1])}")

            if len(vals) == 0 or abs(vals[0] - a[i]) <= 1: 
                vals.append(a[i])
                if i == len(a) - 2 and abs(vals[0] - a[i+1]) <= 1:
                    vals.append(a[i+1])
                    print("Last")
                continue

            count.append(len(vals))
            vals.clear()

    count.append(len(vals))

    return max(count)

#print(pickingNumbers([4, 6, 5, 3, 3, 1]))
#print(pickingNumbers([1, 2, 2, 3, 1, 2]))
#print(pickingNumbers([4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1 ,99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4]))

def picking(a):
    unique = set(a)
    unique = list(unique)
    unique.sort()

    count = []
    pairs = []

    if len(unique) == 1:
        return len(a)

    for i in range(len(unique) - 1):
        print(i, ":", unique[i])
        count.append(a.count(unique[i]))
        if unique[i] + 1 == unique[i+1]:
            pairs.append([unique[i], unique[i+1]])

        if i == len(a) - 2:
            count.append(a.count(unique[i+1]))

    for j in pairs:
        count.append(a.count(j[0]) + a.count(j[1]))

    return max(count)


print(picking([4, 6, 5, 3, 3, 1]))
print(picking([1, 2, 2, 3, 1, 2]))
print(picking([4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1 ,99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4]))
print(picking([4, 97, 5, 97, 97, 4, 97, 4, 97, 97, 97, 97, 4, 4, 5, 5, 97, 5, 97, 99, 4, 97, 5, 97, 97, 97, 5, 5, 97, 4, 5, 97, 97, 5, 97, 4, 97, 5, 4, 4, 97, 5, 5, 5, 4, 97, 97, 4, 97, 5, 4, 4, 97, 97, 97, 5, 5, 97, 4, 97, 97, 5, 4, 97, 97, 4, 97, 97, 97, 5, 4, 4, 97, 4, 4, 97, 5, 97, 97, 97, 97, 4, 97, 5, 97, 5, 4, 97, 4, 5, 97, 97, 5, 97, 5, 97, 5, 97, 97, 97]))

from collections import Counter

def pickingAINumbers(a):
    counts = Counter(a)
    max_length = 0

    for value in counts:
        combined = counts[value] + counts.get(value + 1, 0)
        max_length = max(max_length, combined)

    return max_length

print(pickingAINumbers([4, 6, 5, 3, 3, 1]))
print(pickingAINumbers([1, 2, 2, 3, 1, 2]))
print(pickingAINumbers([4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1 ,99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4]))
print(pickingAINumbers([4, 97, 5, 97, 97, 4, 97, 4, 97, 97, 97, 97, 4, 4, 5, 5, 97, 5, 97, 99, 4, 97, 5, 97, 97, 97, 5, 5, 97, 4, 5, 97, 97, 5, 97, 4, 97, 5, 4, 4, 97, 5, 5, 5, 4, 97, 97, 4, 97, 5, 4, 4, 97, 97, 97, 5, 5, 97, 4, 97, 97, 5, 4, 97, 97, 4, 97, 97, 97, 5, 4, 4, 97, 4, 4, 97, 5, 97, 97, 97, 97, 4, 97, 5, 97, 5, 4, 97, 4, 5, 97, 97, 5, 97, 5, 97, 5, 97, 97, 97]))
