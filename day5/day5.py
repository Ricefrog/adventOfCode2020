#! /usr/bin/python

def getRow(s):
	top = 127
	bot = 0
	for i in range(7):
		print('\ntop: %d, bot: %d' % (top, bot))
		if s[i] == 'F':
			print('F encountered at index %d' % i)
			top = (top - bot + 1) // 2 - 1 + bot
			print('top is now %d' % top)
		else:
			print('B encountered at index %d' % i)
			bot = ((top - bot + 1) // 2) + bot 
			print('bot is now %d' % bot)
	print('before return top: %d, bot: %d' % (top, bot))
	if s[6] == 'F':
	  return bot
	else:
	  return top

def getCol(s):
	top = 7
	bot = 0
	for i in range(7, 9):
		print('\ntop: %d, bot: %d' % (top, bot))
		if s[i] == 'R':
			bot = (top - bot + 1) // 2 + bot
		else:
			top = (top - bot) // 2 + bot
	print('before return top: %d, bot: %d' % (top, bot))
	if s[9] == 'R':
	  return top
	else:
	  return bot
			

inFile = open('input.txt')

seats = []
allSeats = []
for i in range(128):
	allSeats.append([0, 0, 0, 0, 0, 0, 0, 0])
maxID = 0
IDs = []
for line in inFile.readlines():
	seats.append(line)
for seat in seats:
	allSeats[getRow(seat)][getCol(seat)] = 1
	curID = getRow(seat) * 8 + getCol(seat)
	IDs.append(curID)
	if curID > maxID:
		maxID = curID
missing = []
for i in range(128):
	for j in range(8):
		if allSeats[i][j] == 0:
			curID = i * 8 + j
			if curID + 1 in IDs and curID - 1 in IDs:
				missing.append([i, j])
			
print()
print()
getRow('FBFBBFFRLR')
getCol('FBFBBFFRLR')
print()
print(maxID)

print(missing)
'''
newIDs = []
IDs.sort()
for i in IDs:
	if i not in newIDs:
		newIDs.append(i)
for i in range(len(newIDs)):
	if newIDs[i] != newIDs[i + 1] - 1:
		print('id is between %d and %d' % (newIDs[i], newIDs[i + 1]))
'''

print()
print()

print('ids of missing.')
for pair in missing:
	curID = pair[0] * 8 + pair[1]
	if curID + 1 in IDs and curID - 1 in IDs:
		print(curID, 'row: %d, col: %d' % (pair[0], pair[1]))
	else:
		print('did not meet criteria')

getCol('BFFFBBFRRL')
