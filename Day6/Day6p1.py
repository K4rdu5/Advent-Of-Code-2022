#Day 6 part 1
from collections import Counter

with open("day6.txt", "r") as f:
    data = f.read()

i = 0
j = 4
for n in range(len(data)):
    if len(data[i+n:j+n]) < 4:
        break
    freq = Counter(data[i+n:j+n])
    if len(freq) == len(data[i+n:j+n]):
        print(j+n)
        break
