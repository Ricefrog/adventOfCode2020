#! /usr/bin/python

def getMD(directions):
	position = [0, 0] # east/west, north/south
	waypoint = [10, 1]
	directionMap = ['E', 'S', 'W', 'N']
	directionIndex = 0
	for direction in directions:
		op = direction[0]
		val = int(direction[1:])
		print('\nop: %s, val: %d' % (op, val))
		print('waypoint', waypoint)
		print('position', position)
		if op == 'F':
			position[0] += waypoint[0] * val
			position[1] += waypoint[1] * val
		if op == 'N':
			waypoint[1] += val
		elif op == 'S':
			waypoint[1] -= val
		elif op == 'E':
			waypoint[0] += val
		elif op == 'W':
			waypoint[0] -= val
		elif op == 'R':
			ind = val // 90
			wd = ['', '']
			lVal = waypoint[0]
			rVal = waypoint[1]
			waypointCopy = waypoint.copy()

			if waypointCopy[0] >= 0:
				wd[0] = 'E'
			else:
				wd[0] = 'W'
			lInd = directionMap.index(wd[0])
			lInd = (lInd + ind) % 4
			if directionMap[lInd] == 'N':
				if wd[0] == 'S' or wd[0] == 'W':
					waypoint[1] = -1 * lVal
				else:
					waypoint[1] = lVal
			elif directionMap[lInd] == 'S':
				if wd[0] == 'N' or wd[0] == 'E':
					waypoint[1] = -1 * lVal
				else:
					waypoint[1] = lVal
			elif directionMap[lInd] == 'E':
				if wd[0] == 'S' or wd[0] == 'W':
					waypoint[0] = -1 * lVal
				else:
					waypoint[0] = lVal
			elif directionMap[lInd] == 'W':
				if wd[0] == 'E' or wd[0] == 'N':
					waypoint[0] = -1 * lVal
				else:
					waypoint[0] = lVal

			if waypointCopy[1] >= 0:
				wd[1] = 'N'
			else:
				wd[1] = 'S'
			rInd = directionMap.index(wd[1])
			rInd = (rInd + ind) % 4
			print('%s becomes %s' % (wd[1], directionMap[rInd]))
			if directionMap[rInd] == 'N':
				if wd[1] == 'S' or wd[1] == 'W':
					waypoint[1] = -1 * rVal
				else:
					waypoint[1] = rVal
			elif directionMap[rInd] == 'S':
				if wd[1] == 'N' or wd[1] == 'E':
					waypoint[1] = -1 * rVal
				else:
					waypoint[1] = rVal
			elif directionMap[rInd] == 'E':
				if wd[1] == 'S' or wd[1] == 'W':
					waypoint[0] = -1 * rVal
				else:
					waypoint[0] = rVal
			elif directionMap[rInd] == 'W':
				if wd[1] == 'E' or wd[1] == 'N':
					waypoint[0] = -1 * rVal
				else:
					waypoint[0] = rVal
				
		elif op == 'L':
			ind = -1 * (val // 90) 
			print('ind', ind)
			wd = ['', '']
			lVal = waypoint[0]
			rVal = waypoint[1]
			waypointCopy = waypoint.copy()

			if waypointCopy[0] >= 0:
				wd[0] = 'E'
			else:
				wd[0] = 'W'
			lInd = directionMap.index(wd[0])
			lInd += ind
			if lInd < 0:
				lInd = 4 + lInd
			if directionMap[lInd] == 'N':
				if wd[0] == 'S' or wd[0] == 'W':
					waypoint[1] = -1 * lVal
				else:
					waypoint[1] = lVal
			elif directionMap[lInd] == 'S':
				if wd[0] == 'N' or wd[0] == 'E':
					waypoint[1] = -1 * lVal
				else:
					waypoint[1] = lVal
			elif directionMap[lInd] == 'E':
				if wd[0] == 'S' or wd[0] == 'W':
					waypoint[0] = -1 * lVal
				else:
					waypoint[0] = lVal
			elif directionMap[lInd] == 'W':
				if wd[0] == 'E' or wd[0] == 'N':
					waypoint[0] = -1 * lVal
				else:
					waypoint[0] = lVal

			if waypointCopy[1] >= 0:
				wd[1] = 'N'
			else:
				wd[1] = 'S'
			rInd = directionMap.index(wd[1])
			print('rInd', rInd)
			rInd += ind
			if rInd < 0:
				rInd = 4 + rInd
			print('%s becomes %s' % (wd[1], directionMap[rInd]))
			if directionMap[rInd] == 'N':
				if wd[1] == 'S' or wd[1] == 'W':
					waypoint[1] = -1 * rVal
				else:
					waypoint[1] = rVal
			elif directionMap[rInd] == 'S':
				if wd[1] == 'N' or wd[1] == 'E':
					waypoint[1] = -1 * rVal
				else:
					waypoint[1] = rVal
			elif directionMap[rInd] == 'E':
				if wd[1] == 'S' or wd[1] == 'W':
					waypoint[0] = -1 * rVal
				else:
					waypoint[0] = rVal
			elif directionMap[rInd] == 'W':
				if wd[1] == 'E' or wd[1] == 'N':
					waypoint[0] = -1 * rVal
				else:
					waypoint[0] = rVal
	return position


inFile = open('input.txt')

directions = inFile.readlines()
for i in range(len(directions)):
	s = directions[i].replace('\n', '')
	directions[i] = s

print(getMD(directions))

