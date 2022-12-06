import sys

line = sys.stdin.readline().rstrip()
for i in range(0, len(line), 1):
    if len(line[i:i + 14]) == len(set("".join(set(line[i:i + 14])))):
        print(i+14)
        break
