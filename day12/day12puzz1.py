import sys
import re
from path import *

hill = []

line = sys.stdin.readline().strip()
while line:
    hill.append(line)
    line = sys.stdin.readline().strip()

path = Path(hill)
print(path)

path.seek()


