import sys
import re


def getcol(columnNumber):
    print("Kukkuu")
    column = []
    for idx, row in enumerate(intrees):
        column.append(row[columnNumber])
    return column


def countScenicScore(rowOrCol):
    # print("Kotkot", rowOrCol)
    visible = 0

    # print("row:", rowOrCol)
    for idxc, col in enumerate(rowOrCol):

        if idxc <= 0 or idxc >= len(rowOrCol) - 1: continue  # Do not consider edges

        # Count visible trees from left. # Need to do it from right to left
        listLeftReversed = rowOrCol[0:idxc]
        listLeftReversed.reverse()
        visible = 0
        for idxl, val in enumerate(listLeftReversed):
            visible+=1
            if listLeftReversed[idxl][0] >= rowOrCol[idxc][0]:
                break
        if visible > 0: rowOrCol[idxc][1] *= visible

        # Count visible trees from right
        listRight = rowOrCol[idxc + 1:len(rowOrCol)]
        visible = 0
        for idxr, val in enumerate(listRight):
            visible+=1
            if listRight[idxr][0] >= rowOrCol[idxc][0]:
                break
        if visible > 0: rowOrCol[idxc][1] *= visible

    print("Counts in ", rowOrCol, ": ", visible)
    return visible


def getHighestScenicScore():
    score = 0
    for i in range(len(intrees)):
        for j in range(len(intrees[i])):
            if intrees[i][j][1] > score: score = intrees[i][j][1]
    return score


intrees = []
linenumber = 0

for line in sys.stdin:
    # if linenumber == 0:
    #    linenumber += 1
    #   continue

    if line.startswith("#"): continue
    line = line.strip()
    print(line)

    for idx, height in enumerate(line):
        if idx == 0:
            intrees.append([[height, 1]])
        else:
            intrees[linenumber].append([height, 1])
        # print(linenumber, idx, height)
    linenumber += 1

#print(intrees)

visible = 0
dummy = 0

# Iterate through the tree
# First rows
for idx, row in enumerate(intrees):
    # Row by row
    if idx <= 0 or idx >= len(intrees) - 1: continue  # No need to count first and last row. They remain at 0
    countScenicScore(row)

print("Visible in rows: ", visible)
# Then columns
for idx, row in enumerate(intrees):
    # Skip first and last columns, they've been counted already
    if idx <= 0 or idx >= len(row) - 1: continue
    column = getcol(idx)
    visible += countScenicScore(column)

for i in range(len(intrees)):
    print(intrees[i])

print("Highest Scenic Score: ", getHighestScenicScore())
