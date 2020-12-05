#!/usr/bin/env python3

import sys

def part1(d):
    return max(d)

def part2(d):
    for x in range(min(d), max(d)):
        if x not in d:
            return x

data = [x for x in open(sys.argv[1], "r").read().split("\n")]
sID = []

for line in data:
    R = list(range(0, 128))
    C = list(range(0, 8))
    row = line[:7]
    col = line[-3:]

    for r in row:
        l = int(len(R)/2)
        if r == "F": # LOWER
            R = R[:l]
        elif r == "B": # UPPER
            R = R[l:]
    
    fRow = R[0]

    for c in col:
        l = int(len(C)/2)
        if c == "R": # UPPER 
            C = C[l:]
        elif c == "L": # LOWER
            C = C[:l]

    fCol = C[0]

    sID.append(fRow * 8 + fCol)

print(f"Part 1: {part1(sID)}\nPart 2: {part2(sID)}")
