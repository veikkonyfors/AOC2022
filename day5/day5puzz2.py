import sys

stacks = [[], [], [], [], [], [], [], [], [], [], []]
stack = []
cratestomove=[]

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
            cratefrm = stacks[int(frm) - 1]
            crateto = stacks[int(to) - 1]
            cratestomove = []

            for j in range(int(howmany)):
                print("j"); print(j)
                cratestomove.append(cratefrm.pop())
                print(stacks)

            cratestomove.reverse()
            crateto.extend(cratestomove)
            print(stacks)

answer=''
for i in range(9):
    answer+=answer.join(stacks[i].pop())

print(answer)