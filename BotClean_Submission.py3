def next_move(posr, posc, board):
    # Find the nearest dirty cell
    dirty_cells = [(i, j) for i, row in enumerate(board) for j, val in enumerate(row) if val == 'd']
    if not dirty_cells:
        return  # No action needed if there are no dirty cells

    # Calculate distances to all dirty cells
    distances = [abs(posr - i) + abs(posc - j) for i, j in dirty_cells]
    # Get the closest dirty cell
    closest_dirty_cell = dirty_cells[distances.index(min(distances))]

    # Move towards the closest dirty cell
    if closest_dirty_cell[0] < posr:
        print("UP")
    elif closest_dirty_cell[0] > posr:
        print("DOWN")
    elif closest_dirty_cell[1] < posc:
        print("LEFT")
    elif closest_dirty_cell[1] > posc:
        print("RIGHT")
    else:
        print("CLEAN")

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
