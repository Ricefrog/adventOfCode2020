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
	rotated = [[] for r in rows]
	for i in range(len(rows) - 1, -1, -1):
		rInd = 0
		for ch in rows[i]:
			rotated[rInd].append(ch)
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
			print('tile %d: side %s matches.' % (tileNumber, side))
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
		
	
		

inFile = open('input.txt')

raw_1 = [s for s in inFile.read().split('\n\n')]
raw_1 = raw_1[:-1]
print(raw_1)

tiles = {}
for chunk in raw_1:
	temp = chunk.split('\n')
	curTile = int(temp[0][:-1].split(' ')[1])
	if '' in temp:
		temp.remove('')
	tiles[curTile] = temp[1:]

print(tiles)
squareSize = len(tiles) ** 0.5
print('squareSize:', squareSize)
print()
cornerPieces = {}
print(findMatches(tiles, cornerPieces)) # part 1 answer
print(cornerPieces)
