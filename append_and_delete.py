def newAppendAndDelete(s,t,k):
    if k >= len(s) + len(t): 
        return "Yes"

    if s == t:
        if k >= len(t) * 2 or k % 2 == 0:
            return "Yes"
        else:
            return "No"

    moves = 0

    if len(t) < len(s):
        moves += len(s) - len(t)
        s = s[:-moves]
        if t == s and moves == k:
            return "Yes"
        elif t == s and (k - moves) % 2 == 0:
            return "Yes"
        elif moves >= k and t != s:
            return "No"

    matches = ""
    for i, j in zip(s, t):
        if i == j:
            matches += i
        else:
            break

    if len(matches) > 0:
        moves += len(s) - len(matches)
        if k < moves:
            return "No"
        if len(t) > len(s):
            moves += len(t) - len(matches)
            if k < moves or (k - moves) % 2 != 0:
                return "No"
            elif k == moves:
                return "Yes"
        if matches == t:
            if moves == k or (k - moves) % 2 != 0:
                return "Yes"
            else:
                return "No"

        moves += len(t) - len(matches)
        if k < moves:
            return "No"
        elif k == moves or (k - moves) % 2 != 0:
            return "Yes"
        else: 
            return "No"
        
    else:
        moves += len(s) + len(t)
        if moves > k:
            return "No"
        else: 
            return "Yes"


def aiAppendAndDelete(s,t,k):
    if k >= len(s) + len(t):
        return "Yes"

    p = 0
    for a, b in zip(s, t):
        if a != b:
            break
        p += 1

    min_ops = (len(s) - p) + (len(t) - p)

    if k >= min_ops and (k - min_ops) % 2 == 0:
        return "Yes"
    return "No"

print(aiAppendAndDelete("abc", "abd", 3))      # correct: No
print(aiAppendAndDelete("abcdef", "abc", 1))   # correct: No
print(aiAppendAndDelete("ab", "abcdef", 6))    # correct: Yes
print(aiAppendAndDelete("y", "yu", 2))    # correct: Yes
print(aiAppendAndDelete("ashley", "ash", 2))    # correct: Yes