import sys

max1 = 0
max2 = 0
max3 = 0
sum = 0

for line in sys.stdin:
    if line.rstrip() == '':
        if sum > max3:
            print("Sum3i="+str(sum)+" Max1=" + str(max1) + " Max2=" + str(max2) + " Max3=" + str(max3))
            if sum > max2:
                print("Sum2i="+str(sum)+" Max1=" + str(max1) + " Max2=" + str(max2) + " Max3=" + str(max3))
                if sum > max1:
                    print("Sum1i="+str(sum)+" Max1="+str(max1)+" Max2="+str(max2)+" Max3="+str(max3))
                    max3 = max2
                    max2 = max1
                    max1 = sum
                    sum=0
                else:
                    print("Sum1e="+str(sum)+" Max1=" + str(max1) + " Max2=" + str(max2) + " Max3=" + str(max3))
                    max3 = max2
                    max2 = sum
                    sum=0
            else:
                print("Sum2e=" + str(sum) + " Max1=" + str(max1) + " Max2=" + str(max2) + " Max3=" + str(max3))
                max3=sum
                sum=0
        else:
            print(sum)
        sum=0
    else:
        #print(line.rstrip())
        sum += int(line.rstrip())

# deal with the fine line
print("Final line: Sum=" + str(sum) + " Max1=" + str(max1) + " Max2=" + str(max2) + " Max3=" + str(max3))
if sum > max3:
    if sum > max2:
        if sum > max1:
            max3 = max2
            max2 = max1
            max1 = sum
            sum = 0
            print("Max1=" + str(max1) + "Max2=" + str(max2) + " Max3=" + str(max3))
        else:
            max3 = max2
            max2 = sum
            sum = 0
            print("Max1=" + str(max1) + "Max2=" + str(max2) + " Max3=" + str(max3))
    else:
        max3 = sum
        sum = 0
        print("Max1=" + str(max1) + " Max2=" + str(max2) + " Max3=" + str(max3))

print("Max1=" + str(max1) + " Max2=" + str(max2) + " Max3=" + str(max3))
print("Total: " + str(max1 + max2 + max3))
