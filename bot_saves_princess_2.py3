def nextMove(n, r, c, grid):
    # Find the princess's position
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                p_row, p_col = i, j
                break
    
    # Determine the next move towards the princess
    if p_col < c:
        return "LEFT"
    elif p_col > c:
        return "RIGHT"
    elif p_row < r:
        return "UP"
    elif p_row > r:
        return "DOWN"

# Read input and call the function
n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = [input() for _ in range(n)]

print(nextMove(n, r, c, grid))
