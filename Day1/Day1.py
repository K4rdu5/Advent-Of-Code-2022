#Day 1
from itertools import groupby

with open("day1.txt", "r") as f:
    data = [line for line in f.read().split("\n")]
    # print(data)

grouped = [list(sub) for ele, sub in groupby(data, key = bool) if ele]

most = 0
sec = 0
third = 0

for group in grouped:
    group = list(map(int, group))
    val = sum(group)
    if val > most:
        most = val
    elif val > sec:
        sec = val
    elif val > third:
        third = val
        
print(most)
print(most+sec+third)
