#!/usr/bin/env lua5.4

local function parseInput()
    local num = {}
    for str in io.lines(arg[1]) do
        num[#num+1] = tonumber(str)
    end
    return num
end

local num = parseInput()
local result

for i=1, #num do
    for j=1, #num do
        if num[i] + num[j] == 2020 then
            result = num[i] * num[j]
            break
        end
    end
end

print(result)
