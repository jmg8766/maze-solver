import sys
import os.path
from collections import deque

adj = dict()          # (row, column) -> [(row, column),(row, column),(row, column)]
visited = set([])     # [(row, column), (row, column)] 
prev = dict()         # (row, column) -> (row, column)

# Recursively build an adjacency list
# @param row : the row of the cell being visited
# @param col : the column of the cell being visited
def buildAdjList(row, col):
    visited.add((row, col))
    adj[(row, col)] = []

    if height > row+1 and charArray[row+1][col] != "#": # above
        adj[(row, col)].append((row+1, col))
    if 0 < row and charArray[row-1][col] != "#":        # below
        adj[(row, col)].append((row-1, col))
    if 0 < col and charArray[row][col-1] != "#":        # left
        adj[(row, col)].append((row, col-1))
    if width > col+1 and charArray[row][col+1] != "#":  # right 
        adj[(row, col)].append((row, col+1))

    for neighbor in adj[(row, col)]: 
        if neighbor not in visited: 
            buildAdjList(*neighbor)

# perform bread first search using the adjacency list
def bfs():
    queue = deque([start])
    visited = set([])
    while len(queue) > 0:
        subtree_root = queue.popleft()
        if subtree_root == finish: 
            return
        for neighbor in adj[subtree_root]:
            if neighbor in visited: 
                continue
            if neighbor not in queue:
                prev[neighbor] = subtree_root
                queue.append(neighbor)
        visited.add(subtree_root)

# display usage and exit on invalid input file
# TODO: make an actual usage message
def usage():
    print "invalid input"
    print "usage: python maze-solver.py [file]"
    print "\twhen given a valid maze file, outputs the solution in a 'output' file"
    sys.exit(0)

####################################################################################################
if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]): usage()

with open(sys.argv[1]) as mazeInput:
    charArray = mazeInput.readlines() # charArray[row][col]

if len(charArray) < 1 or len(charArray[0]) < 3: usage()

start = (len(charArray)-1, charArray[-1].find("_"))
finish = (0, charArray[0].find("_")) 

if start[1] == -1 or finish[1] == -1: usage()

width = len(charArray[0])
height = len(charArray)

# build an adjacency list to represent this problem as a graph
buildAdjList(*start)

# if finish isn't in the adjacency list, then there isn't a solution
if not finish in adj.keys():
    print "no solution"
    sys.exit(0)

# perform a breadth-first search to populate the prev dictionary with the shortest path
bfs()

# modify the charArray to display the shortest path
ascii_code = 0 # ascii code for a = 97, z = 122
while True:
    row = finish[0]
    column = finish[1]
    letter = chr((ascii_code%26)+97)
    charArray[row] = charArray[row][:column] + letter + charArray[row][column+1:]
    if(finish == start): break
    ascii_code += 1
    finish = prev[finish]

# write the charArray to an output file
with open("output", "w") as mazeOutput:
    for line in charArray:
        mazeOutput.write(line)
