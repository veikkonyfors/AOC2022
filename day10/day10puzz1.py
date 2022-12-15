import sys

cycle_xval=[[1,1]]

for line in sys.stdin:
    line = line.strip()
    print(line)

    if line =="noop":
        new_cycle_xval=[cycle_xval[len(cycle_xval)-1][0] + 1, cycle_xval[len(cycle_xval)-1][1]]
    else:
        cmd, x = line.split(" ")
        new_cycle_xval = [cycle_xval[len(cycle_xval) - 1][0] + 1, cycle_xval[len(cycle_xval) - 1][1]]
        cycle_xval.append(new_cycle_xval)
        new_cycle_xval = [cycle_xval[len(cycle_xval) - 1][0] + 1, cycle_xval[len(cycle_xval) - 1][1]+int(x)]
    cycle_xval.append(new_cycle_xval)
    print(cycle_xval)

signal_strenght = cycle_xval[19][0]*cycle_xval[19][1] + \
    cycle_xval[59][0]*cycle_xval[59][1] + \
    cycle_xval[99][0]*cycle_xval[99][1] + \
    cycle_xval[139][0] * cycle_xval[139][1] + \
    cycle_xval[179][0] * cycle_xval[179][1] + \
    cycle_xval[219][0] * cycle_xval[219][1]


print(signal_strenght)





