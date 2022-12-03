#Day 3
char = []
for line in open("day3.txt", "r"):
    com1 = line[:(len(line))//2]
    com2 = line[(len(line))//2:]
    for case in com1:
        if case in com2:
            char.append(case)
            break
s1 = []
s1 += [ord(c) - 96 if c == c.lower() else (ord(c.lower()) - 96 + 26) for c in char]
print(sum(s1))
