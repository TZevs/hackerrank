import math

def squares(a, b):
    baseA = math.ceil(math.sqrt(a))
    baseB = math.floor(math.sqrt(b))

    if baseA > baseB:
        return 0

    return baseB - baseA + 1
    

print(squares(3, 9))
print(squares(17, 24))