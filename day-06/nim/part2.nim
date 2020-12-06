from os import paramStr
import strutils, sets

let data = paramStr(1).string.readfile.split("\n\n")

var total = 0

for q in data:
    var u: HashSet[char] = toHashSet(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    for c in q.split():
        u = u * toHashSet(c)

    total += len(u)

echo total
