#Day 3 part 2
sacks = []
for line in open("day3.txt", "r"):
    sacks.append(line.strip("\n"))

groups = []
for i in range(len(sacks)//3):
    groups.append(sacks[i*3:(i*3)+3])

common = []
for group in groups:
    sack1 = group[0]
    sack2 = group[1]
    sack3 = group[2]
    for item in sack1:
        if item in sack2 and item in sack3:
            common.append(item)
            break
            
s2 = []
s2 += [ord(c) - 96 if c == c.lower() else (ord(c.lower()) - 96 + 26) for c in common]
print(sum(s2))
