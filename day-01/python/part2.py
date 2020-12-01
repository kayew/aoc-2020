#!/usr/bin/env python3

import sys

num = [int(i) for i in open(sys.argv[1], 'r').read().split("\n")]
# target = 2020
target = 99920044

def part2():
    for i in num:
        for j in num:
            for k in num:
                if i+j+k == target:
                    return i*j*k

print(part2())