#Day 10 part 1
with open("day10.txt", "r") as f:
    data = [line for line in f.read().split("\n")]

cyc = 0
x = 1
sigstr = []
for line in data:
    if line[:4] == "noop":
        cyc += 1
        if cyc == 20 or cyc == 60 or cyc == 100 or cyc == 140 or cyc == 180 or cyc == 220:
            sigstr.append(cyc*x)
    else:
        op, num = line.split(" ")
        cyc += 1
        if cyc == 20 or cyc == 60 or cyc == 100 or cyc == 140 or cyc == 180 or cyc == 220:
            sigstr.append(cyc*x)
        cyc += 1
        if cyc == 20 or cyc == 60 or cyc == 100 or cyc == 140 or cyc == 180 or cyc == 220:
            sigstr.append(cyc*x)
        x += int(num)
        
print(sum(sigstr))
