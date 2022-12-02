import math
import os

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = []

for line in inFile:
    temp = line.replace("\n","").replace(" ", "")
    myList.append(temp)

print("List: " + str(myList) + "\n")

# Globals
shapePoints = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
lose, draw, win = 0, 3, 6

allScores = {
    'BX': shapePoints['X'] + lose, #1
    'CY': shapePoints['Y'] + lose, #2
    'AZ': shapePoints['Z'] + lose, #3
    'AX': shapePoints['X'] + draw, #4
    'BY': shapePoints['Y'] + draw, #5
    'BZ': shapePoints['Z'] + win, #6
    'CX': shapePoints['X'] + win, #7
    'AY': shapePoints['Y'] + win, #8
    'CZ': shapePoints['Z'] + draw, #9
}

opp = { # [lose, draw, win]
    'A': ['Z', 'X', 'Y'],
    'B': ['X', 'Y', 'Z'],
    'C': ['Y', 'Z', 'X']
}

print("\n========== Part 1 ==========")

total = 0
for duel in myList:
    total += allScores[duel]

print("Total Score: " + str(total) + "\n")

print("\n========== Part 2 ==========")

total2 = 0
for duel in myList:
    second = opp[duel[0]][shapePoints[duel[1]]-1]
    total2 += allScores[duel[0] + second]

print("Total Score: " + str(total2) + "\n")