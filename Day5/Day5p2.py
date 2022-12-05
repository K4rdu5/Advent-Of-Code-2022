#Day 5 part 2
with open("day5.txt", "r") as f:
    data = [line for line in f.read().split("\n\n")]

stacks = { 1: ["R", "N", "F", "V", "L", "J", "S", "M"],
           2: ["P", "N", "D", "Z", "F", "J", "W", "H"],
           3: ["W", "R", "C", "D", "G"],
           4: ["N", "B", "S"],
           5: ["M", "Z", "W", "P", "C", "B", "F", "N"],
           6: ["P", "R", "M", "W"],
           7: ["R", "T", "N", "G", "L", "S", "W"],
           8: ["Q", "T", "H", "F", "N", "B", "V"],
           9: ["L", "M", "H", "Z", "N", "F"]}

moves = data[1]
moves = moves.split("\n")

for move in moves:
    move = move.replace("move ", "").replace(" from ", " ").replace(" to ", " ").split(" ")
    move = [int(x) for x in move]
    fslot = stacks[move[1]]
    tslot = stacks[move[2]]
    addlist = []
    for i in range(move[0]):
        mcrates = fslot.pop()
        addlist.append(mcrates)
    for item in addlist[::-1]:
        tslot.append(item)
        
for i in range(len(stacks)):
    print(stacks[i+1].pop())
