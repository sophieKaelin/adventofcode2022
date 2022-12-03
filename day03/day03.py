import math
import os

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
_list = []

for line in inFile:
    temp = line.replace("\n","")
    _list.append(temp)

print("List: " + str(_list) + "\n")

# Score Calculation:
    # a-z = ascii(x)-96
    # A-Z = ascii(x)-38
def getScore(l):
    if str.isupper(l):
        return ord(letter)-38
    return ord(letter)-96


print("\n========== Part 1 ==========")
score = 0
for sack in _list:
    first, second = sack[:len(sack)//2], sack[len(sack)//2:]
    for letter in first:
        if letter in second:
            score += getScore(letter)
            break

print("Score: " + str(score))

print("\n========== Part 2 ==========")
score2, idx = 0, 0
while idx < len(_list):
    for letter in _list[idx]:
        if letter in _list[idx+1] and letter in _list[idx+2]:
            score2 += getScore(letter)
            break
    idx +=3

print("Score: " + str(score2))