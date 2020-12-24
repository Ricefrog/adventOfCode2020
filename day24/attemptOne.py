#! /usr/bin/python

class Node:
	# color: 1 for black, 0 for white
	def __init__(self, tileDict):
		keys = tileDict.keys()
		tile_id = 0
		while tile_id in tileDict:
			tile_id += 1
		tileDict[tile_id] = self
		self.tile_id = tile_id
		self.color = 0
		self.e = None
		self.se = None
		self.sw = None
		self.w = None
		self.nw = None
		self.ne = None

	def printTile(self):
		print()
		print('tile_id:', self.tile_id)
		if self.e:
			print('East:', self.e.tile_id)
		else:
			print('East: None')
		if self.se:
			print('South east:', self.se.tile_id)
		else:
			print('south east: None')
		if self.sw:
			print('south west:', self.sw.tile_id)
		else:
			print('south west: None')
		if self.w:
			print('west:', self.w.tile_id)
		else:
			print('west: None')
		if self.nw:
			print('north west:', self.nw.tile_id)
		else:
			print('north west: None')
		if self.ne:
			print('north east:', self.ne.tile_id)
		else:
			print('north east: None')
	
	def flip(self):
		if self.color:
			self.color = 0
		else:
			self.color = 1

def execute_instructions(centerTile, instructions, tileDict):
	print(f'\nexecuting {len(instructions)} instructions.')
	currentTile = centerTile
	for i, inst in enumerate(instructions):
		if currentTile.e == None:
			currentTile.e = Node(tileDict)

		if currentTile.se == None:
			currentTile.se = Node(tileDict)

		if currentTile.sw == None:
			currentTile.sw = Node(tileDict)

		if currentTile.w == None:
			currentTile.w = Node(tileDict)

		if currentTile.nw == None:
			currentTile.nw = Node(tileDict)

		if currentTile.ne == None:
			currentTile.ne = Node(tileDict)


		currentTile.e.w = currentTile
		currentTile.e.nw = currentTile.ne
		currentTile.e.sw = currentTile.se

		currentTile.se.nw = currentTile
		currentTile.se.ne = currentTile.e
		currentTile.se.w = currentTile.sw

		currentTile.sw.ne = currentTile
		currentTile.se.nw = currentTile.w
		currentTile.se.e = currentTile.se

		currentTile.w.e = currentTile
		currentTile.w.se = currentTile.sw
		currentTile.w.ne = currentTile.nw

		currentTile.nw.se = currentTile
		currentTile.nw.sw = currentTile.w
		currentTile.nw.e = currentTile.ne

		currentTile.ne.sw = currentTile
		currentTile.ne.se = currentTile.e
		currentTile.ne.w = currentTile.nw

		currentTile.e
		currentTile.e
		currentTile.e

		currentTile.printTile()
		print(f'inst: {inst}')
		if inst == 'e':
			nextTile = currentTile.e
		elif inst == 'se':
			nextTile = currentTile.se
		elif inst == 'sw':
			nextTile = currentTile.sw
		elif inst == 'w':
			nextTile = currentTile.w
		elif inst == 'nw':
			nextTile = currentTile.nw
		elif inst == 'ne':
			nextTile = currentTile.ne
		currentTile = nextTile

	print(f'landed on tile {currentTile.tile_id}')
	tileColor = currentTile.color
	if tileColor == 1:
		firstCol = 'black'
		flipCol = 'white'
	else:
		firstCol = 'white'
		flipCol = 'black'
		
	currentTile.flip()
	print(f'tile has been flipped from {firstCol} to {flipCol}.')

def count_blacks(currentTile):
	count = 0	
	if currentTile.e != None:
		count += currentTile.e.color + count_blacks(currentTile.e)
	if currentTile.se != None:
		count += currentTile.se.color + count_blacks(currentTile.se)
	if currentTile.sw != None:
		count += currentTile.sw.color + count_blacks(currentTile.sw)
	if currentTile.w != None:
		count += currentTile.w.color + count_blacks(currentTile.w)
	if currentTile.ne != None:
		count += currentTile.ne.color + count_blacks(currentTile.ne)
	if currentTile.nw != None:
		count += currentTile.nw.color + count_blacks(currentTile.nw)
	return count
	

inFile = open('input2.txt')
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
tileDict = {}
centerTile = Node(tileDict)	
execute_instructions(centerTile, ['nw', 'w', 'sw', 'e', 'e'], tileDict)
print(centerTile.color)
'''
for instructions in allInstructions:
	execute_instructions(centerTile, instructions, tileDict)
count = 0
for key, val in tileDict.items():
	count += val.color
print(count)
'''
