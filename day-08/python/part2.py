#!/usr/bin/env python3

import sys

data = [x.strip() for x in open(sys.argv[1], "r").readlines()]

def execute(d):
    acc = 0
    visited_pos = set()
    i = 0

    while i not in visited_pos and i < len(data):
        ins = d[i][:3]
        amt = int(d[i][4:])
        if i in visited_pos:
            break
        if ins == "acc":
            visited_pos.add(i)
            acc += amt
            i += 1
        if ins == "jmp":
            visited_pos.add(i)
            i += amt
        if ins == "nop":
            i += 1

    return i, acc

for j in [i for i in range(len(data)) if data[i].startswith("jmp")]:
    data[j] = data[j].replace("jmp", "nop")
    i, acc = execute(data)
    data[j] = data[j].replace("nop", "jmp")
    if i == len(data):
        print(acc)
        break
