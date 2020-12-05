#!/usr/bin/env python3

import sys

def part1(d):
    return max(d)

def part2(d):
    d.sort()
    for x in range(d[0], d[-1]):
        if x not in d:
            return x

data = [x.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1') for x in open(sys.argv[1], "r").read().split("\n")]

sID = []

for line in data:
    fRow = int(line[:7], 2)
    fCol = int(line[-3:], 2)

    sID.append(fRow * 8 + fCol)

print(f"Part 1: {part1(sID)}\nPart 2: {part2(sID)}")
