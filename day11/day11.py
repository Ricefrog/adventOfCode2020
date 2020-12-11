#! /usr/bin/python

inFile = open('input.txt')

def printGrid(grid):
	for i in range(len(grid[0])):
		for j in range(len(grid)):
			print(grid[i][j], end='')
		print()

def coordsExist(i, j, rows, cols):
	if i < 0 or j < 0:
		return False
	if i >= rows or j >= cols:
		return False
	return True

def partOne(lines):
	grid = []
	for row in lines: 
		currentRow = []
		for ch in row:
			if ch != '\n':
				currentRow.append(ch)
		grid.append(currentRow)
	print(grid)
	rows = len(grid)
	cols = len(grid[0])
	print('rows: %d, cols: %d' % (rows, cols))

#printGrid(grid)
	changed = True
	cycles = 0
	while changed:
		cycles += 1
		changed = False
		tempGrid = grid
		newGrid = []

		for i in range(rows):
			currentRow = []
			for j in range(cols):
				currentSeat = tempGrid[i][j]
				adjacents = []
				offsetX = 0
				offsetY = 0
				print()

				topLeft = ''
				offsetX = -1
				offsetY = -1
				print('topLeft')
				while coordsExist(i + offsetX, j + offsetY, rows, cols):
					print('tempGrid[%d][%d] = %s' % (i + offsetX, j + offsetY, tempGrid[i + offsetX][j + offsetY]))
					if tempGrid[i + offsetX][j + offsetY] != '.':
						topLeft = tempGrid[i + offsetX][j + offsetY] 
						break
					offsetX += -1
					offsetY += -1
				adjacents.append(topLeft)

				top = ''
				offsetX = -1
				offsetY = 0
				print('top')
				while coordsExist(i + offsetX, j + offsetY, rows, cols):
					print('tempGrid[%d][%d] = %s' % (i + offsetX, j + offsetY, tempGrid[i + offsetX][j + offsetY]))
					if tempGrid[i + offsetX][j + offsetY] != '.':
						top = tempGrid[i + offsetX][j + offsetY] 
						break
					offsetX += -1
					offsetY += 0
				adjacents.append(top)

				topRight = ''
				offsetX = -1
				offsetY = 1
				print('topRight')
				while coordsExist(i + offsetX, j + offsetY, rows, cols):
					print('tempGrid[%d][%d] = %s' % (i + offsetX, j + offsetY, tempGrid[i + offsetX][j + offsetY]))
					if tempGrid[i + offsetX][j + offsetY] != '.':
						topRight = tempGrid[i + offsetX][j + offsetY] 
						break
					offsetX += -1
					offsetY += 1
				adjacents.append(topRight)

				left = ''
				offsetX = 0
				offsetY = -1
				print('left')
				while coordsExist(i + offsetX, j + offsetY, rows, cols):
					print('tempGrid[%d][%d] = %s' % (i + offsetX, j + offsetY, tempGrid[i + offsetX][j + offsetY]))
					if tempGrid[i + offsetX][j + offsetY] != '.':
						left = tempGrid[i + offsetX][j + offsetY] 
						break
					offsetX += 0
					offsetY += -1
				adjacents.append(left)

				right = ''
				offsetX = 0
				offsetY = 1
				print('right')
				while coordsExist(i + offsetX, j + offsetY, rows, cols):
					print('tempGrid[%d][%d] = %s' % (i + offsetX, j + offsetY, tempGrid[i + offsetX][j + offsetY]))
					if tempGrid[i + offsetX][j + offsetY] != '.':
						right = tempGrid[i + offsetX][j + offsetY] 
						break
					offsetX += 0
					offsetY += 1
				adjacents.append(right)

				botLeft = ''
				offsetX = 1
				offsetY = -1
				print('botLeft')
				while coordsExist(i + offsetX, j + offsetY, rows, cols):
					print('tempGrid[%d][%d] = %s' % (i + offsetX, j + offsetY, tempGrid[i + offsetX][j + offsetY]))
					if tempGrid[i + offsetX][j + offsetY] != '.':
						botLeft = tempGrid[i + offsetX][j + offsetY] 
						break
					offsetX += 1
					offsetY += -1
				adjacents.append(botLeft)

				bot = ''
				offsetX = 1
				offsetY = 0
				print('bot')
				while coordsExist(i + offsetX, j + offsetY, rows, cols):
					print('tempGrid[%d][%d] = %s' % (i + offsetX, j + offsetY, tempGrid[i + offsetX][j + offsetY]))
					if tempGrid[i + offsetX][j + offsetY] != '.':
						bot = tempGrid[i + offsetX][j + offsetY] 
						break
					offsetX += 1
					offsetY += 0
				adjacents.append(bot)

				botRight = ''
				offsetX = 1
				offsetY = 1
				print('botRight')
				while coordsExist(i + offsetX, j + offsetY, rows, cols):
					print('tempGrid[%d][%d] = %s' % (i + offsetX, j + offsetY, tempGrid[i + offsetX][j + offsetY]))
					if tempGrid[i + offsetX][j + offsetY] != '.':
						print('breaking')
						botRight = tempGrid[i + offsetX][j + offsetY] 
						break
					offsetX += 1
					offsetY += 1
				adjacents.append(botRight)

				if currentSeat == 'L' and '#' not in adjacents:
					print('i: %d, j: %d' % (i, j))
					print('currentSeat: %s becomes #' % currentSeat)
					print(adjacents)
					currentRow.append('#')
					changed = True
				elif currentSeat == '#' and adjacents.count('#') >= 5:
					print('i: %d, j: %d' % (i, j))
					print('currentSeat: %s becomes L' % currentSeat)
					print(adjacents)
					currentRow.append('L')
					changed = True
				else:
					print('no change, i: %d, j: %d' % (i, j))
					print('currentSeat: %s' % currentSeat)
					print(adjacents)
					currentRow.append(currentSeat)
			print()
			newGrid.append(currentRow)
#printGrid(newGrid)
		grid = newGrid

	print('cycles: %d' % cycles)
	count = 0
	for i in range(rows):
		for j in range(cols):
			if grid[i][j] == '#':
				count += 1
	return count

				
print(partOne(inFile.readlines()))

