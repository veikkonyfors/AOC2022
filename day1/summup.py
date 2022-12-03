import sys

sum = 0

for line in sys.stdin:

    if line.rstrip() == '':
        print(sum)
        sum=0
    else:
        sum += int(line)
        #print("line: "+line+" sum="+str(sum))

