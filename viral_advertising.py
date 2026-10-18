def viralAdvertising(n):    
    shared = 5
    cumulative= 2

    for day in range(1, n +1 ):
        liked = shared // 2
        cumulative += liked 
        shared = liked * 3

    return cumulative

print(viralAdvertising(5))