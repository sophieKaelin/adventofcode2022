print("\n========== INPUTING FILE ==========")

inFile = open("experimental/users/sophiekaelin/AOC/input.txt")
_list = []

for line in inFile:
  temp = line.replace("\n", "")
  _list.append(temp.split(" "))

class Dir:
  def __init__(self, data, parent):
    self.data = data
    self.child = {}
    self.files = []
    self.parent = parent
    self.size = 0

class File:
  def __init__(self, size, name):
    self.name = name
    self.size = size

print("Input: " + str(_list) + "\n")

print("\n========== Part 1 ==========")

root = Dir("/", None)
cur_dir = root

def updateParentsSize(cur):
  if cur.parent == None:
    return cur.size
  cur.parent.size += cur.size
  return updateParentsSize(cur.parent)

# Map out the directory
for exe in _list:
  if exe[0] == "$" and exe[1] == "cd": # IF command -> CD
    if exe[2] == "/": 
      cur_dir = root
      continue
    elif exe[2] == "..":
      cur_dir = cur_dir.parent
      continue
    elif exe[2] not in cur_dir.child: # Does the parent know about this child dir?
      tmp = Dir(exe[2], cur_dir)
      cur_dir.child.update({exe[2]: tmp})
      cur_dir = tmp
    else: # The child dir is known by parent
      cur_dir = cur_dir.child[exe[2]]
  elif exe[0] != "$": # IF output of LS command
    if exe[0] == "dir":
      cur_dir.child.update({exe[1]: Dir(exe[1], cur_dir)})
    else: # If item is a file
      cur_dir.files.append(File(exe[0], exe[1]))
      cur_dir.size += int(exe[0])
      updateParentsSize(cur_dir) # Update all parents up to root with updated file size

# Find all nodes with total size < 100000 and sum together.
def parseTree(r):
  total = 0
  if r == None:
    return 0
  elif r.size <= 100000:
    total += r.size
  for d in r.child:
    total += parseTree(r.child[d])
  return total

print("Actual is:" + str(parseTree(root)))