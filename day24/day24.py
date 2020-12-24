#! /usr/bin/python

from collections import defaultdict

def def_value():
	return 0

def print_tiles(tileDict):
	for coords, color in tileDict.items():
		if color:
			print(f'{coords}: {color}')
	print()

def execute_instructions(tileDict, instructions):
	current_coords = [0, 0]
	for inst in instructions:
		if inst == 'e':
			dx = 1
			dy = 0
		elif inst == 'w':
			dx = -1
			dy = 0
		elif inst == 'se':
			dx = 1
			dy = -1
		elif inst == 'sw':
			dx = 0
			dy = -1
		elif inst == 'ne':
			dx = 0
			dy = 1
		elif inst == 'nw':
			dx = -1
			dy = 1
		current_coords = [current_coords[0] + dx, current_coords[1] + dy]
	tile_color = tileDict[tuple(current_coords)] 
	if tile_color == 0:
		tileDict[tuple(current_coords)] = 1
	else:
		tileDict[tuple(current_coords)] = 0
	
def get_neighbors(tileDict, coords):
	count = 0
	neighbor_diffs = [(1, 0), (-1, 0), (1, -1), (0, -1), (0, 1), (-1, 1)]
	for dx, dy in neighbor_diffs:
		neighbor_coords = (coords[0] + dx, coords[1] + dy)
		if tileDict[neighbor_coords] == 1:
			count += 1
	return count

def apply_rules(tileDict):
	newTileDict = tileDict.copy()
	for coords, color in tileDict.copy().items():
		number_of_neighbors = get_neighbors(tileDict, coords)
		if color == 1:
			if number_of_neighbors == 0 or number_of_neighbors > 2:
				#print(f'{coords} was flipped from black to white.')
				newTileDict[coords] = 0
			else:
				newTileDict[coords] = 1
		else:
			if number_of_neighbors == 2:
				#print(f'{coords} was flipped from white to black.')
				newTileDict[coords] = 1
			else:
				newTileDict[coords] = 0
	return newTileDict

def part_two(tileDict):
	for i in range(100):
		print(f'Day {i + 1}')
		tileDict = apply_rules(tileDict)
	count = 0
	for key, val in tileDict.items():
		count += val
	print(count)

inFile = open('input.txt')
lines = inFile.read().split('\n')
if lines[-1] == '':
	lines.remove('')
print(lines)

allInstructions = []
for currentLine in lines:
	currentInstructions = []
	ind = 0
	while ind != len(currentLine):
		if (curChar := currentLine[ind]) == 'e':
			currentInstructions.append('e')
		elif (curChar := currentLine[ind]) == 'w':
			currentInstructions.append('w')
		elif (curChar := currentLine[ind]) == 's':
			inst = curChar
			ind += 1
			inst += (curChar := currentLine[ind])
			currentInstructions.append(inst)
		elif (curChar := currentLine[ind]) == 'n':
			inst = curChar
			ind += 1
			inst += (curChar := currentLine[ind])
			currentInstructions.append(inst)
		ind += 1
	allInstructions.append(currentInstructions)
#print(allInstructions)
# 0 for white, 1 for black
tileDict = defaultdict(def_value)

max_x = 300
max_y = 300
for x in range(-1 * max_x, max_x):
	for y in range(-1 * max_y, max_y):
		tileDict[(x, y)] = 0

for instructions in allInstructions:
	execute_instructions(tileDict, instructions)

count = 0
for key, val in tileDict.items():
	if val == 1:
		count += 1
print(count)
print_tiles(tileDict)
part_two(tileDict)
