def pageCount(n, p):
    fromFront = p // 2
    fromBack = (n - p) // 2

    if p == 1 or p == n or p - 1 % 2 == 0:
        return 0
    elif n % 2 == 0 and n - 1 == p:
        return 1 
    
    if fromFront < fromBack:
        return fromFront
    else:
        return fromBack

print(pageCount(6, 5))