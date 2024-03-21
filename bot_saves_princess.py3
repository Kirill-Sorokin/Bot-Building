#!/usr/bin/python

def displayPathtoPrincess(n, grid):
    # Determine bot's and princess's positions
    bot = (n // 2, n // 2)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess = (i, j)

    # Calculate the moves
    moves = []
    vertical = 'UP\n' if bot[0] > princess[0] else 'DOWN\n'
    horizontal = 'LEFT\n' if bot[1] > princess[1] else 'RIGHT\n'

    for _ in range(abs(bot[0] - princess[0])):
        moves.append(vertical)
    for _ in range(abs(bot[1] - princess[1])):
        moves.append(horizontal)

    # Print out all the moves
    for move in moves:
        print(move, end='')

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
