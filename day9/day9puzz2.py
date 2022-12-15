import sys
import grid2

rope = [0 for i in range(9)]
rowStart = 0
colStart = 0

row = [0 for i in range(10)]
col = [0 for i in range(10)]

tail_positions = ["0, 0"]  # Initially at origo


def moveTail():
    for j in range(1, 10):
        # head same row,  2 right
        if col[j - 1] - col[j] == 2 and row[j - 1] == row[j]:
            col[j] += 1
            continue

        # head same row, 2 left
        if row[j - 1] == row[j] and col[j - 1] - col[j] == -2:
            col[j] -= 1
            continue

        # head 1 up, 2 right
        if (row[j - 1] - row[j]) == -1 and col[j - 1] - col[j] == 2:
            row[j] -= 1
            col[j] += 1
            continue

        # Deduced
        # head 1 up, 2 left
        if (row[j - 1] - row[j]) == -1 and col[j - 1] - col[j] == -2:
            row[j] -= 1
            col[j] -= 1
            continue

        # head 1 up, 1 left
        if (row[j - 1] - row[j]) == -1 and col[j - 1] - col[j] == -2:
            row[j] -= 1
            col[j] -= 1
            continue

        # Head 2  up, 1 right
        if (row[j - 1] - row[j]) == -2 and col[j - 1] - col[j] == 1:
            row[j] -= 1
            col[j] += 1
            continue

        # head 2 up, 1 left
        if row[j - 1] - row[j] == - 2 and col[j - 1] - col[j] == -1:
            row[j] -= 1
            col[j] -= 1
            continue

        # head 2 up, on the same col
        if (row[j - 1] - row[j]) == -2 and col[j - 1] == col[j]:
            row[j] -= 1
            continue

        # head 2 up, 2 right
        if (row[j - 1] - row[j]) == -2 and col[j - 1] - col[j] == 2:
            row[j] -= 1
            col[j] += 1
            continue

        # Deduced
        # head 2 up, 2 left
        if (row[j - 1] - row[j]) == -2 and col[j - 1] - col[j] == -2:
            row[j] -= 1
            col[j] -= 1
            continue

        # head 1 down, 2 right
        if row[j - 1] - row[j] == 1 and col[j - 1] - col[j] == 2:
            row[j] += 1
            col[j] += 1
            continue

        # head 1 down, 2 left
        if row[j - 1] - row[j] == 1 and col[j - 1] - col[j] == -2:
            row[j] += 1
            col[j] -= 1
            continue

        #########################
        # input_test2 ok up to L 8, but then comes head down 2, left 1 case, which wasn't honored
        # Let's honor down 2 cases now
        # Head 2  down, 1 right
        if (row[j - 1] - row[j]) == 2 and col[j - 1] - col[j] == 1:
            row[j] += 1
            col[j] += 1
            continue

        # head 2 down, 1 left
        if row[j - 1] - row[j] == 2 and col[j - 1] - col[j] == -1:
            row[j] += 1
            col[j] -= 1
            continue

        # head 2 down, on the same col
        if (row[j - 1] - row[j]) == 2 and col[j - 1] == col[j]:
            row[j] += 1
            continue

        # head 2 down, 2 right
        if (row[j - 1] - row[j]) == 2 and col[j - 1] - col[j] == 2:
            row[j] += 1
            col[j] += 1
            continue

        # head 2 down, 2 left
        if (row[j - 1] - row[j]) == 2 and col[j - 1] - col[j] == -2:
            row[j] += 1
            col[j] -= 1
            continue

    #print("tail_positions.append "+str(row[9]) + ", " + str(col[9]))
    tail_positions.append(str(row[9]) + ", " + str(col[9]))
##############################################################


def move(cmd):
    print(cmd)
    direction, amount = cmd.split(' ')

    if direction == 'R':
        for i in range(int(amount)):
            col[0] += 1
            moveTail()

    if direction == 'U':
        for i in range(int(amount)):
            row[0] -= 1
            moveTail()

        # print(i, j, row, " jälkeen")
        # print(i, j, col, " jälkeen")

    if direction == 'L':
        for i in range(int(amount)):
            col[0] -= 1
            moveTail()

    if direction == 'D':
        for i in range(int(amount)):
            row[0] += 1
            moveTail()

            # print(i, j, row, " jälkeen")
            # print(i, j, col, " jälkeen")


for line in sys.stdin:
    line = line.strip()
    move(line)
    #print(row)
    #print(col)
    #print(tail_positions)

print(set(tail_positions), "\n", len(set(tail_positions)))

