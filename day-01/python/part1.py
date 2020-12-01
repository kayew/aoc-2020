#!/usr/bin/env python3

import sys

num = [int(i) for i in open(sys.argv[1], 'r').read().split("\n")]

def part1():
    for i in num:
        for j in num:
            if i + j == 2020:
                return i * j

print(part1())