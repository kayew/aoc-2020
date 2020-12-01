import os
import strutils

var 
    target: int = 2020
    # target = 99920044
    nums = newSeq[int](0)

for line in lines(paramStr(1)):
    nums.add(parseInt(line))

proc main(): int =
    for i in nums:
        for j in nums:
            if i+j == target:
                # assert i == 73542217
                # assert j == 26377827
                # assert i*j == 1939883877222459
                assert i*j == 970816
                return i*j

echo main()
