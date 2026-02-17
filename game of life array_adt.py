class ArrayADT:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_cell(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        return 0  # luar grid dianggap mati

    def display(self):
        for row in self.data:
            print(" ".join(str(cell) for cell in row))
        print()

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
