#!/usr/bin/env python3

import sys

num = [int(i) for i in open(sys.argv[1], 'r').read().split("\n")]
target = 2020
# target = 99920044

def part1(arr):
    for i in arr:
        for j in arr:
            if i+j == target:
                return i*j

def part2(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                if i+j+k == target:
                    return i*j*k

print(f"Part 1: {part1(num)}, Part 2: {part2(num)}")
