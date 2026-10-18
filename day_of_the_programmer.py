def dayOfProgrammer(year):
    # Number of Days up to September (Excluding Feb)
    days = 215 
    
    if 1700 <= year <= 1917:
        if year % 4 == 0:
            days += 29
        else:
            days += 28
    elif year == 1918:
        days += 14
    elif year >= 1919:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days += 29
        else:
            days += 28
    
    day = 256 - days
    dateReturn = f"{day}.09.{year}"

    if day > 30:
        days += 30
        day = 256 - days
        dateReturn = f"{day}.10.{year}"
        
    return dateReturn

#print(dayOfProgrammer(1918))

def altDayOfProgrammer(year):
    # Special case: 1918 is the transition year (Feb had only 15 days)
    if year == 1918:
        return "26.09.1918"

    if year < 1918:
        is_leap = year % 4 == 0
    else:
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    days_jan_to_aug = 31 + (29 if is_leap else 28) + 31 + 30 + 31 + 30 + 31 + 31
    day_in_september = 256 - days_jan_to_aug

    return f"{day_in_september}.09.{year}"

print(dayOfProgrammer(1879))
