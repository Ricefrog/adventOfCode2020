#! /usr/bin/python
import copy

def printRows(rows):
	for row in rows:
		print(row)

def outOfRange(x, y, z, cubeGrid):
	numberOfLayers = cubeGrid['numberOfLayers']
	width = cubeGrid['width']
	lowestZ = -1 * ((numberOfLayers - 1) // 2) 
	highestZ = (numberOfLayers - 1) // 2 
	if x < 0 or x >= width or y < 0 or y >= width or z < lowestZ or z > highestZ: 
		return True
	else:
		return False

def outOfRange2(x, y, z, w, cubeGrid):
	debugPrint = False
	numberOfLayers = cubeGrid['numberOfLayers']
	width = cubeGrid['width']
	lowestZ = -1 * ((numberOfLayers - 1) // 2) + 1
	highestZ = (numberOfLayers - 1) // 2  - 1
	if x < 0 or x >= width or y < 0 or y >= width or z < lowestZ or z > highestZ or w < lowestZ or w > highestZ: 
		if debugPrint:
			print('x: %d, y: %d, z: %d, w: %d -> is out of range.' % (x, y, z, w))
		return True
	else:
		if debugPrint:
			print('x: %d, y: %d, z: %d, w: %d -> is not out of range.' % (x, y, z, w))
		return False

def countActives(cubeGrid):
	actives = 0
	for layer, rows in cubeGrid.items():
		if type(layer) == int:
			for row in rows:
				actives += row.count('#')
	return actives

def countActives2(cubeGrid):
	actives = 0
	for cords, rows in cubeGrid.items():
		if type(cords) == tuple:
			for row in rows:
				actives += row.count('#')
	return actives


def printCube(cubeGrid):
	numberOfLayers = cubeGrid['numberOfLayers']
	lowest = -1 * ((numberOfLayers - 1) // 2)
	highest = (numberOfLayers - 1) // 2
	zList = [i for i in range(lowest, highest + 1)] 

	for layer in zList:
		print('z =', layer)
		for row in cubeGrid[layer]:
			for ch in row:
				print(ch, end='')
			print()
		print()


def addBuffers(cubeGrid):
	numberOfLayers = cubeGrid['numberOfLayers']
	width = cubeGrid['width']
	# adds a layers of empty cubes on each side.
	nextLowestZ = -1 * ((numberOfLayers - 1) // 2) - 1
	nextHighestZ = (numberOfLayers - 1) // 2 + 1
	nextWidth = width + 2

	emptyRow = ['.' for i in range(nextWidth)]
	'''
	print('\nwidth = %d, nextWidth = %d, emptyRow is' % (width, nextWidth))
	print(emptyRow)
	print('nextLowestZ: %d, nextHighestZ: %d' % (nextLowestZ, nextHighestZ))
	'''
	emptyLayer = [emptyRow.copy() for i in range(nextWidth)]
	for layer, rows in cubeGrid.items():
		if type(layer) == int:
			# first add extra dot to sides of each row
			#print('current layer:', layer)
			#print('rows before:')
			#printRows(rows)
			for i in range(len(rows)):
				#print('rows[%d]' % i, rows[i])
				rows[i].append('.')
				rows[i].insert(0, '.')
				#print('rows[%d]' % i, rows[i])
			#print('rows after loop:')
			#printRows(rows)
			rows.append(emptyRow.copy())
			rows.insert(0, emptyRow.copy())
			#print('rows after rowInsert:')
			#printRows(rows)
			#print()
	

	cubeGrid[nextLowestZ] = copy.deepcopy(emptyLayer)
	cubeGrid[nextHighestZ] = copy.deepcopy(emptyLayer)
	cubeGrid['numberOfLayers'] += 2
	cubeGrid['width'] += 2


def getNeighbors(cubeGrid, currentLayer, pos):
	x = pos[0]
	y = pos[1]
	debugPrint = False

	if debugPrint:
		print('\nFinding neighbors for (%d, %d) on z = %d' % (x, y, currentLayer))

	actives = 0
	for aX in range(x - 1, x + 2):
		for aY in range(y - 1, y + 2):
			if outOfRange(aX, aY, currentLayer + 1, cubeGrid):
				continue
			if cubeGrid[currentLayer + 1][aY][aX] == '#':
				actives += 1
				if debugPrint:
					print('active neighbor found at (%d, %d) on layer %d' % (aX, aY, currentLayer + 1))
	for aX in range(x - 1, x + 2):
		for aY in range(y - 1, y + 2):
			if outOfRange(aX, aY, currentLayer - 1, cubeGrid):
				continue
			if cubeGrid[currentLayer - 1][aY][aX] == '#':
				actives += 1
				if debugPrint:
					print('active neighbor found at (%d, %d) on layer %d' % (aX, aY, currentLayer - 1))
	for aX in range(x - 1, x + 2):
		for aY in range(y - 1, y + 2):
			if outOfRange(aX, aY, currentLayer, cubeGrid):
				continue
			if not (aX == x and aY == y) and debugPrint:
				print('checking (%d, %d)' % (aX, aY))
			if not (aX == x and aY == y) and cubeGrid[currentLayer][aY][aX] == '#':
				actives += 1
				if debugPrint:
					print('active neighbor found at (%d, %d) on layer %d' % (aX, aY, currentLayer))
	return actives


def part_1(cubeGrid):
	for cycles in range(6):
		debugPrint = False
		#printCube(cubeGrid)
		numberOfLayers = cubeGrid['numberOfLayers']
		innerWidth = cubeGrid['width'] 
		#print('innerWidth', innerWidth)
		lowestZ = -1 * ((numberOfLayers - 1) // 2) - 1
		highestZ = (numberOfLayers - 1) // 2 + 1
		addBuffers(cubeGrid)
		currentStateGrid = copy.deepcopy(cubeGrid)

		for z in range(lowestZ, highestZ + 1):
			for col in range(1, innerWidth + 1):
				for row in range(1, innerWidth + 1):
					pos = (col, row)
					activeNeighbors = getNeighbors(cubeGrid, z, pos)
					if debugPrint:
						print('position (%d, %d) layer %d has %d active neighbors.' % (pos[0], pos[1], z, activeNeighbors))

					if currentStateGrid[z][row][col] == '#':
						if activeNeighbors == 2 or activeNeighbors == 3:
							currentStateGrid[z][row][col] = '#'
						else:
							currentStateGrid[z][row][col] = '.'
					elif currentStateGrid[z][row][col] == '.':
						if activeNeighbors == 3:
							currentStateGrid[z][row][col] = '#'
						else:
							currentStateGrid[z][row][col] = '.'
		cubeGrid = copy.deepcopy(currentStateGrid)
		print('%d active cubes after cycle %d' % (countActives(cubeGrid), cycles + 1))

def addBuffers2(cubeGrid):
	numberOfLayers = cubeGrid['numberOfLayers']
	width = cubeGrid['width']
	# adds a layers of empty cubes on each side.
	nextLowestZ = nextLowestW = -1 * ((numberOfLayers - 1) // 2) - 1
	nextHighestZ = nextHighestW = (numberOfLayers - 1) // 2 + 1
	nextWidth = width + 2

	emptyRow = ['.' for i in range(nextWidth)]
	'''
	print('\nwidth = %d, nextWidth = %d, emptyRow is' % (width, nextWidth))
	print(emptyRow)
	print('nextLowestZ: %d, nextHighestZ: %d' % (nextLowestZ, nextHighestZ))
	'''
	emptyLayer = [emptyRow.copy() for i in range(nextWidth)]
	for cord, rows in cubeGrid.items():
		if type(cord) == tuple:
			# first add extra dot to sides of each row
			#print('current layer:', layer)
			#print('rows before:')
			#printRows(rows)
			for i in range(len(rows)):
				#print('rows[%d]' % i, rows[i])
				rows[i].append('.')
				rows[i].insert(0, '.')
				#print('rows[%d]' % i, rows[i])
			#print('rows after loop:')
			#printRows(rows)
			rows.append(emptyRow.copy())
			rows.insert(0, emptyRow.copy())
			#print('rows after rowInsert:')
			#printRows(rows)
			#print()
	

	'''
	cubeGrid[(0, nextLowestW)] = copy.deepcopy(emptyLayer)
	cubeGrid[(0, nextHighestW)] = copy.deepcopy(emptyLayer)

	cubeGrid[(nextLowestZ, nextLowestW)] = copy.deepcopy(emptyLayer)
	cubeGrid[(nextLowestZ, nextHighestW)] = copy.deepcopy(emptyLayer)

	cubeGrid[(nextHighestZ, nextLowestW)] = copy.deepcopy(emptyLayer)
	cubeGrid[(nextHighestZ, nextHighestW)] = copy.deepcopy(emptyLayer)
	'''
	for curZ in range(nextLowestZ, nextHighestZ + 1):
		for curW in range(nextLowestW, nextHighestW + 1):
			if (curZ, curW) not in cubeGrid:
				cubeGrid[(curZ, curW)] = copy.deepcopy(emptyLayer)
				cubeGrid[(curZ, curW)] = copy.deepcopy(emptyLayer)
		
		
	cubeGrid['numberOfLayers'] += 2
	cubeGrid['width'] += 2

def getNeighbors2(cubeGrid, currentLayer, currentW, pos):
	x = pos[0]
	y = pos[1]
	debugPrint = False

	if debugPrint:
		print('\nFinding neighbors for (%d, %d) on z = %d' % (x, y, currentLayer))

	actives = 0
	for aW in range(currentW - 1, currentW + 2):
		for aX in range(x - 1, x + 2):
			for aY in range(y - 1, y + 2):
				if outOfRange2(aX, aY, currentLayer + 1, aW, cubeGrid):
					continue
				if cubeGrid[(currentLayer + 1, aW)][aY][aX] == '#':
					actives += 1
					if debugPrint:
						print('active neighbor found at (%d, %d) on layer %d' % (aX, aY, currentLayer + 1))
		for aX in range(x - 1, x + 2):
			for aY in range(y - 1, y + 2):
				if outOfRange2(aX, aY, currentLayer - 1, aW, cubeGrid):
					continue
				if cubeGrid[(currentLayer - 1, aW)][aY][aX] == '#':
					actives += 1
					if debugPrint:
						print('active neighbor found at (%d, %d) on layer %d' % (aX, aY, currentLayer - 1))
		for aX in range(x - 1, x + 2):
			for aY in range(y - 1, y + 2):
				if outOfRange2(aX, aY, currentLayer, aW, cubeGrid):
					continue
				if not (aX == x and aY == y and aW == currentW) and debugPrint:
					print('checking (%d, %d)' % (aX, aY))
				if not (aX == x and aY == y and aW == currentW) and cubeGrid[(currentLayer, aW)][aY][aX] == '#':
					actives += 1
					if debugPrint:
						print('active neighbor found at (%d, %d) on layer %d' % (aX, aY, currentLayer))
	return actives
							
def part_2(cubeGrid):
	for cycles in range(6):
		debugPrint = False
		#printCube(cubeGrid)
		numberOfLayers = cubeGrid['numberOfLayers']
		innerWidth = cubeGrid['width'] 
		#print('innerWidth', innerWidth)
		lowestZ = -1 * ((numberOfLayers - 1) // 2) - 1
		highestZ = (numberOfLayers - 1) // 2 + 1
		addBuffers2(cubeGrid)
		currentStateGrid = copy.deepcopy(cubeGrid)

		for w in range(lowestZ, highestZ + 1):
			for z in range(lowestZ, highestZ + 1):
				for col in range(1, innerWidth + 1):
					for row in range(1, innerWidth + 1):
						pos = (col, row)
						activeNeighbors = getNeighbors2(cubeGrid, z, w, pos)

						if currentStateGrid[(z, w)][row][col] == '#':
							if activeNeighbors == 2 or activeNeighbors == 3:
								currentStateGrid[(z, w)][row][col] = '#'
							else:
								currentStateGrid[(z, w)][row][col] = '.'
						elif currentStateGrid[(z, w)][row][col] == '.':
							if activeNeighbors == 3:
								currentStateGrid[(z, w)][row][col] = '#'
							else:
								currentStateGrid[(z, w)][row][col] = '.'
		cubeGrid = copy.deepcopy(currentStateGrid)
		print('%d active cubes after cycle %d' % (countActives2(cubeGrid), cycles + 1))
					


inFile = open('input.txt')

lines = [line.strip() for line in inFile.readlines()]

width = len(lines[0])

'''
cubeGrid = {0: [[ch for ch in line] for line in lines]}
cubeGrid['width'] = width
cubeGrid['numberOfLayers'] = 1
for i in range(3):
	addBuffers(cubeGrid)
part_1(cubeGrid)
'''

# (z, w)
cubeGrid = {(0, 0): [[ch for ch in line] for line in lines]}
cubeGrid['width'] = width
cubeGrid['numberOfLayers'] = 1
for i in range(3):
	addBuffers2(cubeGrid)
for key in cubeGrid.keys():
	if type(key) == tuple:
		print(key)
		for row in cubeGrid[key]:
			print(row)
part_2(cubeGrid)
