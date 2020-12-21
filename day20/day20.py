#! /usr/bin/python

import itertools

def printTile(rows):
	for row in rows:
		for ch in row:
			print(ch, end='')
		print()

def flip(rows):
	#print('before flip:', rows)
	flipped = []
	for row in rows:
		flipped.append(row[::-1])
	#print('after flip:', flipped)
	return flipped

def rotateRight(rows):
	'''
	print('before rotation')
	printTile(rows)
	'''
	rotated = ['' for r in rows]
	for i in range(len(rows) - 1, -1, -1):
		rInd = 0
		for ch in rows[i]:
			rotated[rInd] += ch
			rInd += 1
	'''
	print('after rotation')
	printTile(rotated)
	'''
	return rotated

# returns an edge as a string
def getEdge(side, rows):
	#print()
	if side == 'top':
		return rows[0]
	elif side == 'bot':
		return rows[-1]
	elif side == 'right':
		edge = ''
		for row in rows:
			#print('row:', row)
			edge += row[len(row) - 1]
		return edge
	elif side == 'left':
		edge = ''
		for row in rows:
			edge += row[0]
		return edge
	else:
		print('invalid side.')
		return -1

def checkMatches(sideToCheck, rows, tileNumber):
	for side in ['top', 'bot', 'right', 'left']:
		if getEdge(side, rows) == sideToCheck or getEdge(side, rows) == sideToCheck[::-1]:
			#print('tile %d: side %s matches.' % (tileNumber, side))
			return True
	return False

def checkAllSides(sideToCheck, rows, tileNumber):
	dummy = rows.copy()
	if checkMatches(sideToCheck, rows, tileNumber) or checkMatches(sideToCheck, flip(rows), tileNumber):
		return True
	for i in range(3):
		dummy = rotateRight(dummy)
		if checkMatches(sideToCheck, rows, tileNumber) or checkMatches(sideToCheck, flip(rows), tileNumber):
			return True
	return False
		
	

def findMatches(tiles, cornerPieces):
	printDebug = True
	part_1 = 1
	cornerEdgeCombos = list(itertools.product(['top', 'bot'], ['right', 'left']))
	for currentTileNumber in tiles.keys():
		if printDebug:
			print()
			print('checking tile %d' % currentTileNumber)
		currentTile = tiles[currentTileNumber]
		twoCornerEdges = 0
		checkedTiles = [currentTileNumber]
		for edgePair in cornerEdgeCombos:
			if printDebug:
				print('checking:', edgePair)
			edges = 0
			for edge in edgePair:
				testEdge = getEdge(edge, currentTile)
				if printDebug:
					print('testEdge:', testEdge)
				for tileNumber, rows in tiles.items():
					if tileNumber not in checkedTiles:
						#if printDebug:
							#print('comparing tile %d with tile %d edge %s.' % (tileNumber, currentTileNumber, edge))
							#print('checkedTiles:', checkedTiles)
						if checkAllSides(testEdge, rows, tileNumber):
							print('match found.')
							checkedTiles.append(tileNumber)
		if len(checkedTiles) == 3:
			print('checkedTiles', checkedTiles)
			print('this is a corner piece.')
			cornerPieces[currentTileNumber] = [s for s in checkedTiles if s != currentTileNumber]
			part_1 *= currentTileNumber
	return part_1

class tileObject:

	def __init__(self, tileNumber, tileDict):
		self.tileNumber = tileNumber
		self.rows = tileDict[tileNumber]
		self.topEdge = getEdge('top', self.rows)
		self.rightEdge = getEdge('right', self.rows)
		self.botEdge = getEdge('bot', self.rows)
		self.leftEdge = getEdge('left', self.rows)

		self.topTile = 'none'
		for otherTile, otherRows in tileDict.items():
			if otherTile != tileNumber:
				if checkMatches(self.topEdge, otherRows, otherTile):
					self.topTile = otherTile
					break

		self.rightTile = 'none'
		for otherTile, otherRows in tileDict.items():
			if otherTile != tileNumber:
				if checkMatches(self.rightEdge, otherRows, otherTile):
					self.rightTile = otherTile
					break

		self.botTile = 'none'
		for otherTile, otherRows in tileDict.items():
			if otherTile != tileNumber:
				if checkMatches(self.botEdge, otherRows, otherTile):
					self.botTile = otherTile
					break

		self.leftTile = 'none'
		for otherTile, otherRows in tileDict.items():
			if otherTile != tileNumber:
				if checkMatches(self.leftEdge, otherRows, otherTile):
					self.leftTile = otherTile
					break

	def rotateRight(self):
		self.rows = rotateRight(self.rows)
		self.topEdge = getEdge('top', self.rows)
		self.rightEdge = getEdge('right', self.rows)
		self.botEdge = getEdge('bot', self.rows)
		self.leftEdge = getEdge('left', self.rows)
		self.topTile, self.rightTile, self.botTile, self.leftTile = self.leftTile, self.topTile, self.rightTile, self.botTile

	def flipHorizontal(self):
		self.rows = flip(self.rows)
		self.topEdge = getEdge('top', self.rows)
		self.rightEdge = getEdge('right', self.rows)
		self.botEdge = getEdge('bot', self.rows)
		self.leftEdge = getEdge('left', self.rows)
		self.leftTile, self.rightTile = self.rightTile, self.leftTile

	def flipVertical(self):
		flipped = []
		for row in self.rows.copy():
			flipped.insert(0, row)
		self.rows = flipped
		self.topEdge = getEdge('top', self.rows)
		self.rightEdge = getEdge('right', self.rows)
		self.botEdge = getEdge('bot', self.rows)
		self.leftEdge = getEdge('left', self.rows)
		self.topTile, self.botTile = self.botTile, self.topTile
			

	def printTile(self):
		print()
		print('tile:', self.tileNumber)
		printTile(self.rows)

	def printConnectingTiles(self):
		print()
		print('This tile:', self.tileNumber)
		print('topTile:', self.topTile)
		print('rightTile:', self.rightTile)
		print('botTile:', self.botTile)
		print('leftTile:', self.leftTile)

def gridComplete(grid, size):
	for row in grid:
		if len(row) < size:
			return False
	return True

def printGrid(grid, size, tileObjects):
	print('\ngrid:', grid)
	for row in grid:
		for i in range(len(tileObjects[0].rows)):
			for tileNumber in row:
				for tileObject in tileObjects:
					if tileObject.tileNumber == tileNumber:
						currentTileObject = tileObject
						break
				print(currentTileObject.rows[i], end=' ')
			print()
		print()
	

def createGrid(tileObjects, tileDict, size):
	grid = [[] for i in range(size)]
	print(grid)
	# find top left tile
	for tile in tileObjects:
		if tile.topTile == 'none' and tile.leftTile == 'none':
			topLeftTileNumber = tile.tileNumber
	print('topLeftTileNumber:', topLeftTileNumber)
	grid[0].append(topLeftTileNumber)
	currentTileNumber = topLeftTileNumber
	for i in range(size): # rows
		for j in range(size): # columns
			for tileObject in tileObjects:
				if tileObject.tileNumber == currentTileNumber:
					currentTileObject = tileObject
					break
			if currentTileObject.rightTile == 'none':
				# this is the last tile in the row
				#grid[i].append(currentTileNumber)
				break
			for tileObject in tileObjects:
				if tileObject.tileNumber == currentTileObject.rightTile:
					rightTileObject = tileObject
					break

			for k in range(3):
				if i == 0:
					topEdge = rightTileObject.topEdge
				else: 
					aboveTileNumber = grid[i - 1][j + 1]
					for tileObject in tileObjects:
						if tileObject.tileNumber == aboveTileNumber:
							topEdge = tileObject.botEdge

				if currentTileObject.rightEdge == rightTileObject.leftEdge and rightTileObject.topEdge == topEdge:
					break

				rightTileObject.flipHorizontal()
				if currentTileObject.rightEdge == rightTileObject.leftEdge and rightTileObject.topEdge == topEdge:
					break
				rightTileObject.flipHorizontal()

				rightTileObject.flipVertical()
				if currentTileObject.rightEdge == rightTileObject.leftEdge and rightTileObject.topEdge == topEdge:
					break
				rightTileObject.flipVertical()

				rightTileObject.rotateRight()

			grid[i].append(rightTileObject.tileNumber)
			currentTileNumber = rightTileObject.tileNumber
			printGrid(grid, size, tileObjects)

		currentTileNumber = grid[i][0]
		for tileObject in tileObjects:
			if tileObject.tileNumber == currentTileNumber:
				currentTileObject = tileObject
				break
		if currentTileObject.botTile == 'none':
			break
		for tileObject in tileObjects:
			if tileObject.tileNumber == currentTileObject.botTile:
				botTileObject = tileObject
				break
		for k in range(3):
			if currentTileObject.botEdge == botTileObject.topEdge and botTileObject.leftTile == 'none':
				break

			botTileObject.flipHorizontal()
			if currentTileObject.botEdge == botTileObject.topEdge and botTileObject.leftTile == 'none':
				break
			botTileObject.flipHorizontal()

			botTileObject.flipVertical()
			if currentTileObject.botEdge == botTileObject.topEdge and botTileObject.leftTile == 'none':
				break
			botTileObject.flipVertical()

			botTileObject.rotateRight()
		grid[i + 1].append(botTileObject.tileNumber)
		currentTileNumber = botTileObject.tileNumber
		printGrid(grid, size, tileObjects)
	return grid

inFile = open('input.txt')

raw_1 = [s for s in inFile.read().split('\n\n')]
raw_1 = raw_1[:]
if '' in raw_1:
	raw_1.remove('')
print(raw_1)

tiles = {}
for chunk in raw_1:
	temp = chunk.split('\n')
	curTile = int(temp[0][:-1].split(' ')[1])
	if '' in temp:
		temp.remove('')
	tiles[curTile] = temp[1:]

print(tiles)
squareSize = int(len(tiles) ** 0.5)
print('squareSize:', squareSize)
print()
tileObjects = [tileObject(tileNumber, tiles) for tileNumber in tiles.keys()]
for t in tileObjects:
	t.printConnectingTiles()
	print()

'''
tileObjects[0].printTile()
tileObjects[0].printConnectingTiles()
tileObjects[0].flipVertical()
tileObjects[0].printTile()
tileObjects[0].printConnectingTiles()
'''

grid = createGrid(tileObjects, tiles, squareSize)
'''
print([tileObject.tileNumber for tileObject in tileObjects])
for tileObject in tileObjects:
	if tileObject.tileNumber == 1171 or tileObject.tileNumber == 2791:
		tileObject.printTile()
		print(tileObject.rows)
'''

'''
cornerPieces = {}
print(findMatches(tiles, cornerPieces)) # part 1 answer
print(cornerPieces)
'''
