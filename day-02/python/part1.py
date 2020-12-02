#!/usr/bin/env python3

import sys

file = open(sys.argv[1], "r")
total = 0
letterMatch = 0

for line in file:
    param = line.split()
    passRange = param[0].split("-")
    targetLetter = param[1][0]
    password = param[2]

    letterMatch = password.count(targetLetter)
    if letterMatch >= int(passRange[0]) and letterMatch <= int(passRange[1]):
            total += 1
            
print(f"total: {total}")
