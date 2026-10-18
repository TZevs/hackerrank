def gradingStudents(grades):
    finalGrades = []
    print(grades)
    
    for i in grades:
        if i < 38:
            finalGrades.append(i)
        else:
            if (i+2) % 5 == 0:
                finalGrades.append(i+2)
            elif (i+1) % 5 == 0:
                finalGrades.append(i+1)
            else:
                finalGrades.append(i)

    return finalGrades

grades = [44, 84,94,21,0,18,100,18,62,30,61,53,0,43,2,29,53,61,40, 14]
print(gradingStudents(grades))