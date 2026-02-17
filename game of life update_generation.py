def next_generation(grid):
    new_grid = ArrayADT(grid.rows, grid.cols)

    for r in range(grid.rows):
        for c in range(grid.cols):
            neighbors = count_neighbors(grid, r, c)
            cell = grid.get_cell(r, c)

            if cell == 1 and neighbors in (2, 3):
                new_grid.set_cell(r, c, 1)
            elif cell == 0 and neighbors == 3:
                new_grid.set_cell(r, c, 1)
            else:
                new_grid.set_cell(r, c, 0)

    return new_grid
