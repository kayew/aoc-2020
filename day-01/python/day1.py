#!/usr/bin/env python3

import sys

num = [int(i) for i in open(sys.argv[1], 'r').read().split("\n")]

def part1(arr):
    result = 0
    for i in arr:
        for j in arr:
            if i+j == 2020:
                result = i*j
    return result

def part2(arr):
    result = 0
    for i in arr:
        for j in arr:
            for k in arr:
                if i+j+k == 2020:
                    result = i*j*k
    return result

print(f"Part 1: {part1(num)}, Part 2: {part2(num)}")