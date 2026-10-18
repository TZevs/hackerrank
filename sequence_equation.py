def permutationEquation(p):
    n = len(p)
    pos = [0] * (n + 1)

    for i in range(1, n + 1):
        pos[p[i - 1]] = i

    print(p)
    print(pos)
    return [pos[pos[x]] for x in range(1, n + 1)]

print(permutationEquation([5,2,1,3,4])) 