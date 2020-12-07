#!/usr/bin/env python3

import sys
import re

# fmt: off
data = [x.strip().split(" bags contain ") for x in open(sys.argv[1]).readlines()]

for b in data:
    d = {}
    d[b[0]] = b[1].split(", ")
    for k, v in d.items():
        t = []
        for i in range(len(v)):
            if v[i][0] != "n":
                t.append(v[i][2:].split(" bag")[0])
                d[k] = t
            else:
                d[k] = []
                continue

print(d)

