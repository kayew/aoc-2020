from os import paramStr
import strutils, sets

let data = paramStr(1).string.readfile.split("\n\n")

var total = 0

for q in data:
    var u: HashSet[char] = initHashSet[char]()
    for c in q.split():
        u = u + toHashSet(c)

    total += len(u)

echo total
