def migratoryBirds(arr):
    count = [0] * 6

    for bird in arr:
        count[bird] += 1

    max_count = max(count)
    for type in range(1, 6):
        if count[type] == max_count:
            return type

print(migratoryBirds([1, 4, 4, 4, 5, 3]))
print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
