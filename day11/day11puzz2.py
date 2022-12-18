import sys
import re


class Monkey:
    items = []  # Worry levels of items
    operation = ""  # How worry level changes while inspected
    test = 0  # Divisible by this
    true_target = -1  # target if true
    false_target = -1  # target if false
    inspections=0

    def __str__(self):
        return "Monkey: items: " + str(self.items) + " operation: " + str(self.operation) + ", test: " + \
            str(self.test) + " true_target: " + self.true_target + " false_target: " + self.false_target

    def operate_item_bored(self, i):
        self.inspections += 1
        op, val = self.operation.split(" ")
        if val == "old":
            ival=int(self.items[i])
        else:
            ival=int(val)
        if op == "*":
            ival = ival * int(self.items[i])
        else:
            ival = ival + int(self.items[i])

        self.items[i] = ival % mod

    def throw(self,i):
        if (int(self.items[i]) % int(self.test)) == 0:
            monkeys[int(self.true_target)].items.append(self.items[i])
            #print(i, monkey, self.items[i], self.test, " thrown to ", self.true_target)
        else:
            monkeys[int(self.false_target)].items.append(self.items[i])
            #print(i, monkey, self.items[i], self.test, " thrown to ", self.false_target)

    def inspect(self):
        for i in range(len(self.items)):
            self.operate_item_bored(i)
            self.throw(i)
        self.items=[]

monkeys = []

line = sys.stdin.readline().strip()
while line:
    #print(line)

    if line.startswith("Monkey"):
        monkey = Monkey()
        line = sys.stdin.readline().strip()
        monkey.items = [int(eval(i)) for i in line.split(":")[1].split(",")]
        line = sys.stdin.readline().strip()
        monkey.operation = re.sub("Operation: new = old ", "", line)
        line = sys.stdin.readline().strip()
        monkey.test = int(re.sub("Test: divisible by ", "", line))
        line = sys.stdin.readline().strip()
        monkey.true_target = re.sub("If true: throw to monkey ", "", line)
        line = sys.stdin.readline().strip()
        monkey.false_target = re.sub("If false: throw to monkey ", "", line)
        line = sys.stdin.readline().strip()  # Empty line between monkeys
        line = sys.stdin.readline().strip()  # Next monkey

    #print(monkey)
    monkeys.append(monkey)

mod=1
for monkey in monkeys:
    mod *= monkey.test
print(mod)

for round in range(10000):
    print("Round: ", round)
    for monkey in monkeys:
        monkey.inspect()

inspections=[]
for monkey in monkeys:
    #print(monkey.inspections, monkey)
    inspections.append(monkey.inspections)

inspections.sort()
print(inspections)
a=inspections.pop()
b=inspections.pop()

print(a, b, a*b)