def mergeHighDefinitionIntervals(intervals):
    intervals.sort()
    result = [intervals[0]]
    i = 0

    for i in range(1, len(intervals)):
        if result[-1][1] >= intervals[i][0]:
            if result[-1][1] >= intervals[i][1]:
                continue
            last = result.pop(-1)
            result.append([last[0], intervals[i][1]])
        else:
            result.append(intervals[i]) 
    
    return result
    

print(mergeHighDefinitionIntervals([[1,4], [2,3], [3,5], [6,7]]))
print("--------------------------------")
print(mergeHighDefinitionIntervals([[1,2], [2,3], [3,4], [10,20]]))
