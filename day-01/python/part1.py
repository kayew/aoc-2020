#!/usr/bin/env python3

import sys

num = [int(i) for i in open(sys.argv[1], 'r').read().split("\n")]
# target = 2020
target = 99920044


def part1():
    for i in num:
        for j in num:
            if i + j == target:
                return i * j

print(part1())