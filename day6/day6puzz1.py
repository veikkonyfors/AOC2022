import sys

line = sys.stdin.readline().rstrip()
for i in range(0, len(line), 1):
    if len(line[i:i + 4]) == len(set("".join(set(line[i:i + 4])))):
        print(i+4)
        break
