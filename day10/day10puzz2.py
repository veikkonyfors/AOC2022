import sys

cycle_xval = [[1, 1]]

crt = [['.' for i in range(40)] for j in range(6)]

for line in sys.stdin:
    line = line.strip()
    print(line)

    if line == "noop":
        new_cycle_xval = [cycle_xval[len(cycle_xval) - 1][0] + 1, cycle_xval[len(cycle_xval) - 1][1]]
    else:
        cmd, x = line.split(" ")
        new_cycle_xval = [cycle_xval[len(cycle_xval) - 1][0] + 1, cycle_xval[len(cycle_xval) - 1][1]]
        cycle_xval.append(new_cycle_xval)
        new_cycle_xval = [cycle_xval[len(cycle_xval) - 1][0] + 1, cycle_xval[len(cycle_xval) - 1][1] + int(x)]
    cycle_xval.append(new_cycle_xval)
    print(cycle_xval)

signal_strenght = cycle_xval[19][0] * cycle_xval[19][1] + \
                  cycle_xval[59][0] * cycle_xval[59][1] + \
                  cycle_xval[99][0] * cycle_xval[99][1] + \
                  cycle_xval[139][0] * cycle_xval[139][1] + \
                  cycle_xval[179][0] * cycle_xval[179][1] + \
                  cycle_xval[219][0] * cycle_xval[219][1]

# selataan cyclet läpi 0-239
for cycle in range(240):
    # Jos sprite on +-1 cyclestä, niin pistetään pixeli crt:lle
    if cycle_xval[cycle][1] - 1 <= cycle-int(cycle/40)*40 <= cycle_xval[cycle][1] + 1:
        cycle_xval[cycle][1] = '#'
        print(cycle, int(cycle/40), cycle-int(cycle/40)*40)
        crt[int(cycle/40)][cycle-int(cycle/40)*40] = '#'

print(cycle_xval)

for j in range(6):
    print(crt[j])

# FPGPHFGH