from collections import defaultdict

def queensAttack(n, k, r_q, c_q, obstacles):
    by_first = defaultdict(list)
    by_second = defaultdict(list)

    for tup in obstacles:
        first, second = tup

        if first < n and second < n:
            by_first[first].append(second)
            by_second[second].append(first)

    moves = 0

    # For the "row" the queen is in
    if r_q in by_first:
        if len(by_first[r_q]) == 1:
            moves += n - by_first[r_q][0] - 1
        else: 
            # Get the closest obstacle to the queen from the bottom of the board
            lower = max((x for x in by_first[r_q] if x < r_q), default=0)
            # Get the closest obstacle from the queen to the top of the board
            upper = min((x for x in by_first[r_q] if x > r_q), default=n)

            moves += upper - lower - 1
    else: 
        moves += n - 1

    print("After Row:", moves)

    # For the "col" the queen is in
    if c_q in by_second:
        if len(by_second[c_q]) == 1:
            moves += n - by_second[c_q][0] - 1
        else:
            # Get the closest obstacle to the queen from the left of the board
            left = max((x for x in by_second[c_q] if x < c_q), default=0)
            # Get the closest obstacle from the queen from the right of the board
            right = min((x for x in by_second[c_q] if x > c_q and x < n), default=0)

            if right == 0: 
                moves += n - left - 1
            else:
                moves += right - left - 1
    else:
        moves += n - 1

    print("After Col:", moves)
    # Remove the row and column obstacles from the tuple list
    noRowCol = [(x, y) for x, y in obstacles if x != r_q and y != c_q]
    # Remove the non-diagonal obstacles
    diags = [(x, y) for x, y in noRowCol if abs(x - r_q) == abs(y - c_q)]
    print(diags)

    if len(diags) > 0:
        bottomLeft = [(x, y) for x, y in diags if x < r_q and y < c_q]
        bottomRight = [(x, y) for x, y in diags if x < r_q and y > c_q]
        topLeft = [(x, y) for x, y in diags if x > r_q and y < c_q]
        topRight = [(x, y) for x, y in diags if x > r_q and y > c_q]

        if len(bottomLeft) > 0:
            closestBottomLeft = max(bottomLeft, key=lambda x: x[0])
            moves += (r_q - closestBottomLeft[0] - 1) + (c_q - closestBottomLeft[1] - 1)
        else:
            moves += r_q - 1

        if len(bottomRight) > 0:
            closestBottomRight = max(bottomRight, key=lambda x: x[0])
            moves += (r_q - closestBottomRight[0] - 1) + (c_q - closestBottomRight[1] - 1)
        else:
            moves += r_q - 1

        if len(topLeft) > 0:
            closestTopLeft = min(topLeft, key=lambda x: x[0])
            moves += (r_q - closestTopLeft[0] - 1) + (c_q - closestTopLeft[1] - 1)
        else:
            moves += r_q - 1

        if len(topRight) > 0:
            closestTopRight = min(topRight, key=lambda x: x[0])
            moves += (r_q - closestTopRight[0] - 1) + (c_q - closestTopRight[1] - 1)
        else:
            moves += r_q - 1

    else:
        # Check bottom left diagonal
        if 1 <= r_q - 1 and 1 <= c_q - 1:
            moves += min(r_q - 1, c_q - 1)
        # Check bottom right diagonal
        if 1 <= r_q - 1 and c_q + 1 <= n:
            moves += min(r_q - 1, n - c_q)
        # Check top left diagonal
        if 1 <= r_q + 1 and 1 <= c_q - 1:
            moves += min(n - r_q, c_q - 1)
        # Check top right diagonal
        if 1 <= r_q + 1 and c_q + 1 <= n:
            moves += min(n - r_q, n - c_q)

    return moves

#print(queensAttack(5, 3, 4, 3, [(5,5), (4,2), (2,3)]))  # Output: 10

def aiQueensAttack(n, k, r_q, c_q, obstacles):
    # Create a set of obstacles for O(1) lookups
    obstacle_set = set((r, c) for r, c in obstacles)
    print("Obstacle Set:", obstacle_set)

    moves = 0

    # Directions the queen can move: vertical, horizontal, and diagonal
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),  # vertical and horizontal
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # diagonals
    ]

    for dr, dc in directions:
        r, c = r_q + dr, c_q + dc
        while 1 <= r <= n and 1 <= c <= n and (r, c) not in obstacle_set:
            moves += 1
            r += dr
            c += dc

    return moves

print(aiQueensAttack(5, 3, 4, 3, [(5,5), (4,2), (2,3)]))  

def claudeQueensAttack(n, k, r_q, c_q, obstacles):
    # Max reachable squares in each direction, keyed by (dr, dc)
    limits = {
        (1, 0):   n - r_q,
        (-1, 0):  r_q - 1,
        (0, 1):   n - c_q,
        (0, -1):  c_q - 1,
        (1, 1):   min(n - r_q, n - c_q),
        (1, -1):  min(n - r_q, c_q - 1),
        (-1, 1):  min(r_q - 1, n - c_q),
        (-1, -1): min(r_q - 1, c_q - 1),
    }

    for r, c in obstacles:
        dr, dc = r - r_q, c - c_q
        if dr == 0 or dc == 0 or abs(dr) == abs(dc):
            step = (
                (dr > 0) - (dr < 0),
                (dc > 0) - (dc < 0),
            )
            dist = max(abs(dr), abs(dc))
            # Squares attackable before hitting this obstacle
            if dist - 1 < limits[step]:
                limits[step] = dist - 1

    return sum(limits.values())

