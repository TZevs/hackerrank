def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = 0
    orangeCount = 0
    
    for i in apples:
        aPos = a + i
            
        if aPos >= s and aPos <= t:
            appleCount += 1

    for j in oranges:
        oPos = b + j
        
        if oPos >= s and oPos <= t:
            orangeCount += 1 
        
    print(appleCount)
    print(orangeCount)
    return

countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])