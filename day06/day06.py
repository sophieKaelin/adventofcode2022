print("\n========== INPUTTING FILE ==========")

inFile = open("input.txt")
inp = ""

for line in inFile:
    inp = line.replace("\n","")

print("List: " + inp + "\n")

print("\n========== Part 1 ==========")

def checkUniqueChar(input):
    for i in input:
        if input.count(i)>1:
            return False
    return True

mark = 3
while mark < len(inp):
    if checkUniqueChar(inp[mark-3:mark+1]):
        break
    mark += 1

print("Marker: " + str(mark+1))

print("\n========== Part 2 ==========")

def uniqueOptimised(input, r):
    for i in input:
        if input.count(i)>1:
            r = i
            return False
    return True

mark = 14
repeated = '*'
while mark < len(inp):
    sub = inp[mark-13:mark+1]
    if not sub.count(repeated) > 1 and uniqueOptimised(sub, repeated):
        break
    mark += 1

print("Marker: " + str(mark+1))