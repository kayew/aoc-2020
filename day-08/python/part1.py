#!/usr/bin/env python3

import sys

data = [x for x in open(sys.argv[1], "r").readlines()]

acc = 0
visted_pos = set()
i = 0

while True:
    ins = data[i][:3]
    if i in visted_pos:
        break
    if ins == "acc":
        visted_pos.add(i)
        acc += int(data[i][4:])
        i += 1
        continue
    if ins == "jmp":
        visted_pos.add(i)
        i += int(data[i][4:])
        continue
    if ins == "nop":
        i += 1
        continue

print(acc)
