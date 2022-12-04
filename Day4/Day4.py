#Day 4
with open("day4.txt","r") as f:
    data = [line for line in f.read().split("\n")]

p1 = 0
p2 = 0
p3 = 0
for d in data:
    i1, i2 = d.split(",")
    s1, e1 = i1.split("-")
    s2, e2 = i2.split("-")
    s1 = int(s1)
    s2 = int(s2)
    e1 = int(e1)
    e2 = int(e2)
    if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
        p1 += 1
    if not (e2 < s1 or e1 < s2):
        p2 += 1
print(p1)
print(p2)
