def divisibleSumPairs(n, k, ar):
    count = 0
   
    for i in range(n - 1):
        for j in range(i + 1, n):
            if i < j and (ar[i] + ar[j]) % k == 0:
                count += 1
    
    return count

arr = [
    43, 95, 51, 55, 40, 86, 65, 81, 51, 20,
    47, 50, 65, 53, 23, 78, 75, 75, 47, 73,
    25, 27, 14, 8, 26, 58, 95, 28, 3, 23,
    48, 69, 26, 3, 73, 52, 34, 7, 40, 33,
    56, 98, 71, 29, 70, 71, 28, 12, 18, 49,
    19, 25, 2, 18, 15, 41, 51, 42, 46, 19,
    98, 56, 54, 98, 72, 25, 16, 49, 34, 99,
    48, 93, 64, 44, 50, 91, 44, 17, 63, 27,
    3, 65, 75, 19, 68, 30, 43, 37, 72, 54,
    82, 92, 37, 52, 72, 62, 3, 88, 82, 71
]

print(divisibleSumPairs(100, 22, arr))

def optimisedDivisiblePairs(n, k, ar):
    remainder_count = [0] * k

    for num in ar:
        remainder_count[num % k] += 1

    count = 0
    # Counts how many pairs are in the index 0 remainder bucket, combinations formula
    count += remainder_count[0] * (remainder_count[0] - 1) // 2

    for r in range(1, k//2 - 1):
        if r != k - r:
            count += remainder_count[r] * remainder_count[k - r]
        else:
            count += remainder_count[r] * (remainder_count[r] - 1) // 2

    return count