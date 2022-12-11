#Day 10 part 2
with open("day10.txt", "r") as f:
    data = [line for line in f.read().split("\n")]
    
def insprite(cyc, sprite):
    if cyc in sprite:
        return True
    return False

s = ""
cyc = 0
x = 1
sprite = [x-1, x, x+1]
for line in data:
    if line[0:4] == "noop":
        if insprite(cyc,sprite):
            s += "#"
        else:
            s += "."
        cyc += 1
        if cyc == 40:
            cyc = 0
            s += "\n"
    else:
        if insprite(cyc,sprite):
            s += "#"
        else:
            s += "."
        cyc += 1
        if cyc == 40:
            cyc = 0
            s += "\n"

        if insprite(cyc,sprite):
            s += "#"
        else:
            s += "."
        cyc += 1
        if cyc == 40:
            cyc = 0
            s += "\n"

        _, num = line.split(" ")
        x += int(num)
        sprite = sprite = [x-1, x, x+1]
print(s)
