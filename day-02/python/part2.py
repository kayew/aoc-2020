#!/usr/bin/env python3

import sys

file = open(sys.argv[1], "r")
total = 0

for line in file:
    letterMatch = 0
    param = line.split()
    passIndex = param[0].split("-")
    targetLetter = param[1][0]
    password = param[2]

    if password[int(passIndex[0])-1] == targetLetter:
        letterMatch += 1
    if password[int(passIndex[1])-1] == targetLetter:
        letterMatch += 1

    if letterMatch == 1:
        total += 1

print(f"total: {total}")
