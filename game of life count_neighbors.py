def count_neighbors(grid, row, col):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    count = 0
    for dr, dc in directions:
        count += grid.get_cell(row + dr, col + dc)
    return count
