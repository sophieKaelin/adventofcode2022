import re
import copy

print("\n========== INPUTTING FILE ==========")

inFile = open("input.txt")
_list = [['R', 'P', 'C', 'D', 'B', 'G'], ['H', 'V', 'G'], ['N', 'S', 'Q', 'D', 'J', 'P', 'M'], ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'], ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'], ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'], ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'], ['C', 'M', 'D', 'B', 'F'], ['F', 'C', 'Q', 'G']]
instr = [] # [number, source, dest]

for line in inFile:
    temp = line.replace("\n","")
    instr.append([int(x) for x in re.split("move | from | to ", temp)[1:]])

print("\n========== Part 1 ==========")
tempStack = copy.deepcopy(_list)
for _in in instr:
    for i in range(_in[0]):
        tempStack[_in[2]-1].append(tempStack[_in[1]-1].pop())

result = ""
for stack in tempStack:
    result += stack[-1]

print("Spells: " + result)

print("\n========== Part 2 ==========")
tempStack = copy.deepcopy(_list)
for _in in instr:
    temp = []
    for i in range(_in[0]):
        temp.insert(0, tempStack[_in[1]-1].pop())
    tempStack[_in[2]-1].extend(temp)

result = ""
for stack in tempStack:
    result += stack[-1]

print("Spells: " + result)