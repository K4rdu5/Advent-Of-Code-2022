#Day 2 part 2

with open("day2.txt", "r") as f:
    data = [line for line in f.read().split("\n")]
    data = data[:-1]

#X loss, Y draw, Z win
out = {"X":0, "Y":3, "Z":6}
win = {"A":2, "B":3, "C":1}
loss = {"A":3, "B":1, "C":2}
draw = {"A":1, "B":2, "C":3}

tot = 0
for game in data:
    op, res = game.split(" ")
    points = out[res]
    if points == 6:
        tot += points + win[op]
    elif points == 3:
        tot += points + draw[op]
    elif points == 0:
        tot += points + loss[op]
print(tot)
