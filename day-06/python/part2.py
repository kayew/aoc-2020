#!/usr/bin/env python3

import sys
import string

data = [x for x in open(sys.argv[1]).read().split("\n\n")]

total = 0

for q in data:
    u = set([x for x in string.ascii_lowercase])
    for c in q.split():
        u = u.intersection(set([x for x in c]))
    
    total += len(u)
    
print(total)
