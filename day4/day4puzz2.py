import sys

sum = 0

for line in sys.stdin:
    sec1, sec2 = line.rstrip().split(",")
    sec1_s, sec1_e = sec1.split("-")
    sec2_s, sec2_e = sec2.split("-")
    print(sec1, sec2, sec1_s, sec1_e, sec2_s, sec2_e)

    if int(sec2_s) <= int(sec1_s) <= int(sec2_e) or \
        int(sec1_s) <= int(sec2_s) <= int(sec1_e) or \
        int(sec2_s) <= int(sec1_e) <= int(sec2_e) or \
        int(sec1_s) <= int(sec2_e) <= int(sec1_e):


        sum += 1
        print(sum)

print(sum)
