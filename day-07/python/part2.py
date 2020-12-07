#!/usr/bin/env python3

import sys
import re

# fmt: off
data = [x.strip().split(" bags contain ") for x in open(sys.argv[1]).readlines()]

d = {}

for b in data:
    d[b[0]] = b[1].split(", ")

for k,v in d.items():
    t = []
    for i in v:
        if i[0] != "n":
            t.append((i[2:].split(" bag")[0], int(i[0])))
            d[k] = t
        else:
            d[k] = []
            continue

