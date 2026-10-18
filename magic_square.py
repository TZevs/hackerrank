def formingMagicSquare(s):
    valid = [
        [8,1,6, 3,5,7, 4,9,2],
        [6,1,8, 7,5,3, 2,9,4],
        [4,9,2, 3,5,7, 8,1,6],
        [2,9,4, 7,5,3, 6,1,8],
        [8,3,4, 1,5,9, 6,7,2],
        [4,3,8, 9,5,1, 2,7,6],
        [6,7,2, 1,5,9, 8,3,4],
        [2,7,6, 9,5,1, 4,3,8]
    ]

    sFlat = [el for row in s for el in row]
    count = []

    for matrix in valid:
        sum = 0
        for idx, val in enumerate(sFlat):
            if matrix[idx] == val:
                continue
            else:
                sum += (abs(matrix[idx] - val))

        count.append(sum)

    return min(count)

print(formingMagicSquare([[5,3,4], [1,5,8], [6,4,2]]))