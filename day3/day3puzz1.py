import sys

sum = 0

for line in sys.stdin:
    x = len(line) // 2;
    # print(line[:x], line[x:], sep="\n")

    c1 = line[:x]
    c2 = line[x:]
    common = ''.join(set(c1).intersection(c2))
    # print(common)
    if len(common) == 1:
        print(common)
        if common.isupper():
            print(ord(common) - 64 + 26)
            sum+=ord(common) - 64 + 26
        else:
            print(ord(common) - 96)
            sum+=ord(common) - 96


print(sum)

