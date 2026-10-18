def nonDivisibleSubset(k, s):
    buckets = [0] * k

    for num in s:
        buckets[num % k] += 1

    max_subset = 0

    combos = [(i, k - i) for i in range(1, (k // 2) + 1)]

    for i, j in combos:
        if i == j:
            max_subset += 1
        else:
            max_subset += max(buckets[i], buckets[j])

    if buckets[0] > 0:
        max_subset += 1

    return max_subset

print(nonDivisibleSubset(3, [1, 7, 2, 4]))
print(nonDivisibleSubset(4, [19, 10, 12, 10, 24, 25, 22]))

