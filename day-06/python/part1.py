#!/usr/bin/env python3

import sys

data = [x.replace("\n", "") for x in open(sys.argv[1]).read().split("\n\n")]

total = 0

for q in data:
    u = set()
    for c in q:
        u.add(c)
    
    total += len(u)
    
print(total)
