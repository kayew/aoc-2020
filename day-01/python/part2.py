#!/usr/bin/env python3

import sys

num = [int(i) for i in open(sys.argv[1], 'r').read().split("\n")]

for i in num:
    for j in num:
        for k in num:
            if i+j+k == 2020:
                print(i*j*k)
