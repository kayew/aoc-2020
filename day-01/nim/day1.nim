import os
import strutils
import strformat

var 
    target: int = 2020
    nums = newSeq[int](0)

for line in lines(paramStr(1)):
    nums.add(parseInt(line))

proc part1(arr: seq, tar: int): int =
    for i in arr:
        for j in arr:
            if i+j == tar:
                return i*j

proc part2(arr: seq, tar: int): int =
    for i in arr:
        for j in arr:
            for k in arr:
                if i+j+k == tar:
                    return i*j*k


echo fmt"Part 1: {part1(nums, target)}, Part 2: {part2(nums, target)}"
