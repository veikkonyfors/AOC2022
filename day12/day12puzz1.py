import sys
import re
from path import *

hill = []

line = sys.stdin.readline().strip()
while line:
    hill.append(line)
    line = sys.stdin.readline().strip()

path = Path(hill)
#print(path)

path.find_start()
path.find_end()

print(path.start_row, path.start_col, path.end_row, path.end_col)

path.seek()

for p in path.all_paths: print("Path:\n",p, " Valid: ", p.valid, " Count: ", p.count)


