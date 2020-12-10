#!/usr/bin/env python3

import sys

adapter_list = [0] + [int(x.strip()) for x in open(sys.argv[1], "r").readlines()]
adapter_list.sort()

adapter_range = list(range(1, 4))
diff_1 = 0
diff_3 = 0
highest = adapter_list[-1] + 3
adapter_list.append(highest)

for i in range(len(adapter_list)-1):
    if adapter_list[i+1] - adapter_list[i] == 3:
        diff_3 += 1
    if adapter_list[i+1] - adapter_list[i] == 1:
        diff_1 += 1

print(f"{diff_1} * {diff_3} = {diff_3 * diff_1}")
