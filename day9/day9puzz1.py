import sys
import grid

grid = grid.FixedGrid()

for line in sys.stdin:
    line = line.strip()
    grid.move(line)


print(grid.grid)
print("countT", grid.countLocT())


