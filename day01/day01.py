
import math
import os

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
elves = [0]
elfIdx = 0

for line in inFile:
    temp = line.replace("\n","")
    if not temp: # New Elf !
        elves.append(0)
        elfIdx +=1
    else: # Update existing elf with calories.
        elves[elfIdx] += int(temp)

print("Number of Elves: " + str(elfIdx+1))
print("Elves + Calories: " + str(elves) + "\n")

print("\n========== Part 1 ==========")
max1 = max(elves)
print("Max Calories is: " + str(max1) + "\n")

print("\n========== Part 2 ==========")
elves.remove(max1)
max2 = max(elves)
elves.remove(max2)
max3 = max(elves)

print("Max Sum of Calories from top 3 is: " + str(max1 + max2 + max3) + "\n")