import os
import sequtils
import strformat

var 
    data: seq[string] = toSeq(lines(paramStr(1)))
    slope: tuple = (3, 1)
    numRows: int = len(data)
    numCols: int = len(data[0])
    trees: int = 0
    x: int = 0

for y in countup(0, numRows-1, slope[1]):
    if data[y][x] == '#':
        trees += 1
    x = (x + slope[0]) mod numCols

echo fmt"trees: {trees}"
