def circularArrayRotation(a, k, queries):
    b = []

    if k == len(a):
        b = a
    elif k < len(a):
        b = a[-k:] + a[:-k]
    elif k > len(a):
        fullRotations = k // len(a)
        left = k - fullRotations * len(a)
        b = a[-left:] + a[:-left]
    
    requested = []
    for i in queries:
        requested.append(b[i])
    
    return requested

print(circularArrayRotation(
    [39356, 87674, 16667, 54260, 43958, 70429, 53682, 6169, 
     87496, 66190, 90286, 4912, 44792, 65142, 36183, 43856, 
     77633, 38902, 1407, 88185, 80399, 72940, 97555, 23941, 
     96271, 49288, 27021, 32032, 75662, 69161, 33581, 15017, 
     56835, 66599, 69277, 17144, 37027, 39310, 23312, 24523, 
     5499, 13597, 45786, 66642, 95090, 98320, 26849, 72722, 
     37221, 28255, 60906], 
    51, [47, 10, 12, 13, 6, 29, 22, 17, 7, 3, 30, 45, 1, 21, 50, 17, 25, 42]))
print("====")
print(circularArrayRotation([1,2,3], 2, [0,1,2]))

def AIcircularArrayRotation(a, k, queries):
    n = len(a)
    k = k % n

    return [a[(i - k) % n] for i in queries]