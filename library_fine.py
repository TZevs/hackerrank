def libraryFine(d1, m1, y1, d2, m2, y2):
    if (y1 < y2) or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 < d2) or (y1 == y2 and m1 == m2 and d1 == d2):
        return 0
    elif y2 < y1:
        return 10000
    
    if m1 == m2:
        return 15 * (d1 - d2)
    else:
        return 500 * (m1 - m2)
    
print(libraryFine(2, 7, 1014, 1, 1, 1014))
print(libraryFine(2, 7, 1014, 1, 1, 1015))