import sys
import re

dirs = {}
cwd = 0

for line in sys.stdin:
    line = line.strip()
    print(line)

    if line.startswith("$ cd"):
        if line == "$ cd /":
            dirs = {"/": 0}
            cwd = "/"
        else:
            if ".." in line:
                cwd = '/'.join(cwd.split("/")[:-1])
            else:
                cwd += "/" + line.split(' ')[2]
                dirs[cwd] = 0

    if line[0].isdigit():
        dirs[cwd] += int(line.split(" ")[0])
        cwdup = '/'.join(cwd.split("/")[:-1])
        while cwdup != "":
            dirs[cwdup] += int(line.split(" ")[0])
            cwdup = '/'.join(cwdup.split("/")[:-1])

print(dirs)

free = 70000000 - dirs["/"]
required = 30000000 - free
print(free, required)
selectedsize = dirs["/"]

for dir in dirs:
    # print(dir, dirs[dir])
    if dirs[dir] >= required:
        print(dir, dirs[dir])
        if dirs[dir] < selectedsize:
            selectedsize = dirs[dir]

print(required, selectedsize)
