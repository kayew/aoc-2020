import os
import strutils

var 
    target = 2020
    nums = newSeq[int](0)

for line in lines(paramStr(1)):
    nums.add(parseInt(line))

proc main(): int =
    for i in nums:
        for j in nums:
            for k in nums:
                if i+j+k == target:
                    return i*j*k

echo main()
