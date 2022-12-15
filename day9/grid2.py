# Kesken. Dynaaminen allokaatio gridille.
# Ei taivu nyt.
# Pitää kokeilla fixatulla gridillä
import sys


class FixedGrid:
    def __init__(self):

        self.MAX_ROWS = 19
        self.MAX_COLS = 19

        self.rows = 0
        self.row = [self.MAX_ROWS/2 for i in range(10)]
        self.col = [self.MAX_ROWS / 2 for i in range(10)]
        self.row[0] = int(self.MAX_ROWS/2)
        self.col[0] = int(self.MAX_COLS/2)
        self.row[1] = int(self.MAX_ROWS/2)
        self.col[1] = int(self.MAX_COLS/2)
        self.grid = [['' for i in range(self.MAX_COLS)] for j in range(self.MAX_ROWS)]
        self.moves=0

    def move(self, cmd):
        direction, amount = cmd.split(' ')
        print(direction, amount)
        self.moves+=1

        print("row[0], col[0], row[1], col[1]: ", self.row[0], self.col[0], self.row[1], self.col[1])

        if direction == 'R':
            for i in range(int(amount)):
                if self.col[0] >= self.MAX_COLS - 1:
                    print("MAX_COLS, col[0]:",self.col[0])
                    sys.exit(1)

                self.col[0] += 1  # Keep 1 behind
                if abs(self.col[0] - self.col[1]) > 1:  # [1] is more than one col behind [0]
                    self.col[1] += 1
                    if self.row[1] != self.row[0]:  # If not on the same row, move needs to be diagonal
                        self.row[1] = self.row[0]
                self.grid[self.row[1]][self.col[1]] = self.moves

        if direction == 'L':
            for i in range(int(amount)):
                #if self.col[0] >= self.MAX_COLS - 1: sys.exit("MAX_COLS")
                if self.col[0] < 0:
                    print("MIN_COLS, col[0]:",self.col[0])
                    sys.exit(1)
                self.col[0] -= 1  # Keep 1 behind
                if abs(self.col[0] - self.col[1]) > 1:  # [1] is more than one col behind [0]
                    self.col[1] -= 1
                    if self.row[1] != self.row[0]:  # If not on the same row, move needs to be diagonal
                        self.row[1] = self.row[0]
                self.grid[self.row[1]][self.col[1]] = self.moves

        if direction == 'U':
            for i in range(int(amount)):
                if self.row[0] >= self.MAX_ROWS - 1: sys.exit("MAX_ROWS")
                #if self.row[0] < 0: sys.exit("MIN_ROWSS")
                self.row[0] += 1
                if abs(self.row[0] - self.row[1]) > 1:  # [1] is more than one row behind [0]
                    self.row[1] += 1  # Keep 1 behind
                    if self.col[1] != self.col[0]:  # if not on same column, move diagonally
                        self.col[1] = self.col[0]
                self.grid[self.row[1]][self.col[1]] = self.moves

        if direction == 'D':
            for i in range(int(amount)):
                #if self.row[0] >= self.MAX_ROWS - 1: sys.exit("MAX_ROWS")
                if self.row[0] < 0: sys.exit("MIN_ROWS")
                self.row[0] -= 1
                if abs(self.row[0] - self.row[1]) > 1:  # [1] is more than one row behind [0]
                    self.row[1] -= 1  # Keep 1 behind
                    if self.col[1] != self.col[0]:  # if not on same column, move diagonally
                        self.col[1] = self.col[0]
                self.grid[self.row[1]][self.col[1]] = self.moves

        print("row[0], col[0], row[1], col[1]: ",self.row[0], self.col[0], self.row[1], self.col[1])
    def countT(self):
        count=0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != '': count+=1

        return count

