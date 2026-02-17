grid = ArrayADT(5, 5)

# Pola awal (blinker)
grid.set_cell(2, 1, 1)
grid.set_cell(2, 2, 1)
grid.set_cell(2, 3, 1)

print("Generasi Awal:")
grid.display()

for i in range(4):
    grid = next_generation(grid)
    print(f"Generasi {i+1}:")
    grid.display()
