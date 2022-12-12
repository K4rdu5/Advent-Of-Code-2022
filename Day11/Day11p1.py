#Day 11 part 1
import math

with open("day11.txt", "r") as f:
    data = [monkey for monkey in f.read().split("\n\n")]

def tester(item, test):
    if item % test == 0:
        return True
    return False

refined = []
for monkey in data:
    monkey, startitems, op, test, ifyes, ifnot = monkey.split("\n ")
    monkey = monkey[7]
    startitems = startitems.strip("Starting items: ").split(", ")
    op = op[12:].split(" ")
    test = int(test.strip("Test: divisible by "))
    ifyes = ifyes.strip("If true: throw to monkey ")
    ifnot = ifnot.strip("If false: throw to monkey ")
    data = [monkey, startitems, op, test, ifyes, ifnot]
    refined.append(data)

counter = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0}
for i in range(20):
    for i, items in enumerate(refined):
        monkey = items[0]
        op = items[2]
        test = int(items[3])
        ifyes = int(items[4])
        ifnot = int(items[5])
        local = 0
        for item in refined[i][1]:
            local += 1
            counter[monkey] += 1
            if op[2] == op[4]:
                new = int(item)*int(item)
            elif op[3] == "+":
                new = int(item) + int(op[4])
            elif op[3] == "-":
                new = int(item) - int(op[4])
            elif op[3] == "*":
                new = int(item) * int(op[4])
            else:
                new = int(item) / int(op[4])
            item = math.floor(int(new)/3)
            if tester(item,test):
                refined[ifyes][1].append(item)
            else:
                refined[ifnot][1].append(item)

        for _ in range(local):
            refined[i][1].pop(0)

twobig = sorted(counter.values())[-2:]
print(twobig[0]*twobig[1])
