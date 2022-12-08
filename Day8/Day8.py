#Day 8
import numpy as np

grid = np.array([list(line.strip()) for line in open("day8.txt", "r")], int)
rows, cols = np.shape(grid)

def is_vis(tree, up, down, left, right):
    if tree > max(up) or tree > max(down) or tree > max(left) or tree > max(right):
        return True
    return False

def score(tree, up, down, left, right):
    us = 0
    for t in up[::-1]:
        us += 1
        if tree <= t:
            break
    ds = 0
    for t in down:
        ds += 1
        if tree <= t:
            break
    ls = 0
    for t in left[::-1]:
        ls += 1
        if tree <= t:
            break
    rs = 0
    for t in right:
        rs += 1
        if tree <= t:
            break
    return us * ds * ls * rs

vis = 4 * len(grid) - 4
scores = []
for i in range(1,rows-1):
    for j in range(1,cols-1):
        tree = grid[i, j]
        up = grid[:i, j]
        down = grid[i+1:,j]
        left = grid[i,:j]
        right = grid[i,j+1:]
        if is_vis(tree, up, down, left, right):
            vis += 1
        scores.append(score(tree, up, down, left, right))

print(vis)
print(max(scores))
