import math
import os

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
_list = []

for line in inFile:
    temp = line.replace("\n","").split(",")
    _list.append([[int(x) for x in temp[0].split("-")], [int(x) for x in temp[1].split("-")]])

print("Lists: " + str(_list) + "\n")

print("\n========== Part 1 ==========")

count = 0
for p in _list:
    if p[0][0] >= p[1][0] and p[0][1] <= p[1][1]:
        count += 1
    elif p[1][0] >= p[0][0] and p[1][1] <= p[0][1]:
        count += 1

print("Count of contains: " + str(count) + "\n")

print("\n========== Part 2 ==========")

count2 = 0
for p in _list:
    if p[1][0] <= p[0][0] <= p[1][1] or p[1][0] <= p[0][1] <= p[1][1]:
        count2 +=1
    elif p[0][0] <= p[1][0] <= p[0][1] or p[1][1] <= p[0][1] <= p[1][0]:
        count2 +=1

print("Count of contains: " + str(count2) + "\n")