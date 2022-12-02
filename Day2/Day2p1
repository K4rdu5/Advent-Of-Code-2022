#Day 2 part 1

with open("day2.txt", "r") as f:
    data = [line for line in f.read().split("\n")]
    data = data[:-1]

val = {"X":1, "Y":2, "Z":3}
def score(op, me):
    if op == "A" and me == "X" or op == "B" and me == "Y" or op == "C" and me == "Z":
        return 3
    if (op == "A" and me == "Z") or (op == "B" and me == "X") or (op == "C" and me =="Y"):
        return 0
    return 6

tot = 0
for game in data:
    op, me = game.split(" ")
    tot += score(op, me) + val[me]
print(tot)
