#!/usr/bin/env lua5.4

local function parseInput()
    local num = {}
    for str in io.lines(arg[1]) do
        num[#num+1] = tonumber(str)
    end
    return num
end

local num = parseInput()
local target = 2020
-- local target = 99920044

local function part1(arr)
    for i=1, #arr do
        for j=1, #arr do
            if arr[i] + arr[j] == target then
                return arr[i] * arr[j]
            end
        end
    end
end

local function part2(arr)
    for i=1, #arr do
        for j=1, #arr do
            for k=1, #arr do
                if arr[i] + arr[j] + arr[k] == target then
                    return arr[i] * arr[j] * arr[k]
                end
            end
        end
    end
end

print("Part 1: "..part1(num)..", Part 2: "..part2(num))
