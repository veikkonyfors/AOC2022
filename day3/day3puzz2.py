import sys

sum = 0
n=0
group=[]

for line in sys.stdin:
    #print(line, n, sep=", ")
    group.append(line.rstrip())
    n+=1
    if n==3:
        print(group)
        common = ''.join(
            set(group[0]).intersection(group[1]))
        common = ''.join(
            set(common).intersection(group[2]))
        print(common)

        if common.isupper():
            print(ord(common) - 64 + 26)
            sum+=ord(common) - 64 + 26
        else:
            print(ord(common) - 96)
            sum+=ord(common) - 96

        group=[]
        n=0


print(group)
"""
common = ''.join(
    set(group[0]).intersection(group[1]))
common = ''.join(
    set(common).intersection(group[2]))
print(common)

if common.isupper():
    print(ord(common) - 64 + 26)
    sum += ord(common) - 64 + 26
else:
    print(ord(common) - 96)
    sum += ord(common) - 96
"""
print(sum)

