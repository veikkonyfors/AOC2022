import sys

max=0
sum=0

for line in sys.stdin:
 if line.rstrip()=='':
   if sum>max:
      max=sum
   sum=0
   print("Max="+str(max))
 else:
   sum+=int(line)
 print(line.rstrip())

print("Max="+str(max))
