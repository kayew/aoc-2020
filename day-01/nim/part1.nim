import os
import strutils
import sequtils
import strformat

var 
    target: int = 2020
    # target = 99920044
    nums = toSeq(lines(paramStr(1))).mapit(parseInt it)

proc main(): seq = 
    for i in nums:
        for j in nums:
            if i+j == target:
                # assert i == 73542217
                # assert j == 26377827
                # assert i*j == 1939883877222459
                assert i*j == 970816
                return @[i,j,i*j]
            
var result = main()
echo fmt"{result[0]} * {result[1]} = {result[2]}"