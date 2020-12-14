#! /usr/bin/python

def findNearest(departTime, temp):
	IDs = []
	for ID in temp:
		if ID != 'x':
			IDs.append(int(ID))
	print(IDs)
	nears = {}
	for ID in IDs:
		temp = 0
		while temp < departTime:
			temp += ID
		nears[temp] = ID

	print(nears)

	gaps = {}
	for key, val in nears.items():
		gaps[val] = key - departTime
	print(gaps)


def findFactors(ID_dict):
	# switch ID and offset
	reverseID_dict = {}
	offsets = []
	for key, val in ID_dict.items():
		offsets.append(val)
		reverseID_dict[val] = int(key)
	offsets.sort()
	factor = reverseID_dict[offsets[0]]
	offsets = offsets[1:]
	print()
	print(offsets)
	print(reverseID_dict)
	print('first factor: %d' % factor)

	for offset in offsets:
		print('offset: %d' % offset)
		y = 1
		curMultiple = reverseID_dict[offset] * factor
		print('curMultiple = %d' % curMultiple)
		while (reverseID_dict[offset] * y) % curMultiple != offset:
			y += 1
		factor = curMultiple
		print('factor is now %d' % factor)
		
	return factor


		

def gcd(x, y):
	mults = x // y
	remainder = x % y
	print('\nx %d, y %d' % (x, y))
	print('mults %d, remainder %d' % (mults, remainder))
	if remainder == 0:
		return y
	return gcd(y, remainder)

def meetsSubs(timestamp, ID_dict, mainMod):
	for key, val in ID_dict.items():
		temp = int(key) * (timestamp // int(key)) + int(key)
		if temp % timestamp != val:
			return False
	return True


def subsequents(IDs):
	ID_dict = {}
	for i in range(len(IDs)):
		if IDs[i] != 'x':
			print('Bus ID %s departs %d minutes after t.' % (IDs[i], i))
			ID_dict[IDs[i]] = i
	mainMod = findFactors(ID_dict)
	print(mainMod)
	return
	y = 1
	timestamp = mainMod * y
	while not meetsSubs(timestamp, ID_dict, mainMod):
		print('y: %d' % y)
		print('timestamp: %d' % timestamp)
		y += 1
		timestamp = mainMod * y
	return timestamp
	
inFile = open('input2.txt')

temp = inFile.read().split('\n')
departTime = int(temp[0])

IDs = []
for line in temp[1:]:
	IDs.append(line.split(','))
IDs = IDs[0]
print(departTime)
print(findNearest(departTime, IDs))
print(subsequents(IDs))
