def jumpingOnClouds(c, k):
    e = 100
    n = len(c)

    pos = 0

    if n % k == 0:
        for i in range(0, n, k):
            e -= 1
            
            if c[i] == 1:
                e -= 2
    else:
        while True:
            pos += k
            if pos > n - 1:
                diff = pos - n
                pos = diff 

            e -= 1
            if c[pos] == 1:
                e -= 2

            if pos == 0:
                break

    return e

# print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))
# print(jumpingOnClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3))

def altJumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = 0

    while True:
        i = (i + k) % n
        e -= 1

        if c[i] == 1:
            e -= 2

        if i == 0:
            break

    return e


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))
print(jumpingOnClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3))