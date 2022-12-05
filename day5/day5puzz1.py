import sys

stacks = [[], [], [], [], [], [], [], [], [], [], []]
stack = []

for line in sys.stdin:
    line = line.rstrip()
    if "[" in line:
        #print(line)
        for i in range(len(line)):
            #print(i, line[i])
            if line[i] == "[":
                index = int(i/4)
                print(i, index)
                stack = stacks[index]
                stack.insert(0,line[i + 1])
                stacks[index] = stack
                print(stacks)
    else:
        print(line)
        if "move" in line:
            skp1, howmany, skp2, frm, skp3, to = line.split(' ')
            print(howmany, frm, to)
            for j in range(int(howmany)):
                print("j"); print(j)
                cratefrm = stacks[int(frm)-1]
                crateto = stacks[int(to)-1]
                crateto.append(cratefrm.pop())
                print(stacks)

answer=''
for i in range(9):
    answer+=answer.join(stacks[i].pop())

print(answer)