#Day 7
from collections import defaultdict

with open("day7.txt", "r") as f:
    data = [line for line in f.read().split("\n")]

path = []
folder = defaultdict(int)
for line in data:
    seg = line.strip().split()
    if seg[1] == "cd":
        if seg[2] == "..":
            path.pop()
        else:
            path.append(seg[2])
    elif seg[0].isdigit():
        size = seg[0]
        for i in range(len(path)):
            folder["/".join(path[:i+1])] += int(size)
print(sum(f for f in folder.values() if f <= 100000))

#Part 2
used = max(folder.values())
free = 70000000 - used
needed = 30000000 - free
mindel = min([f for f in folder.values() if f >= needed])
print(mindel)
