#! /usr/bin/python

inFile = open('input.txt')

fields = inFile.read().split('\n\n')

print(fields[0])

types = fields[0].split('\n')
print(types)	

typesDict = {}
for line in types:
	endInd = line.find(':')
	typeName = line[:endInd]
	print('typeName', typeName)
	temp1 = line[endInd + 1:].split('or')
	temp1 = [l.strip() for l in temp1]
	firstRange = [int(l) for l in temp1[0].split('-')]
	secondRange = [int(l) for l in temp1[1].split('-')]
	typesDict[typeName] = [firstRange, secondRange]
print(typesDict)

otherTickets = fields[2].split('\n')[1:-1]
print(otherTickets)

invalidValues = []
validTickets = []
for tick in otherTickets:
	nums = tick.split(',')

	valid = True 
	for num in nums:
		invalids = 0
		curNum = int(num)

		for key, ranges in typesDict.items():
			firstRange = ranges[0]
			secondRange = ranges[1]
			print()
			print('type: %s' % key)
			print(firstRange)
			print(secondRange)

			if (curNum < firstRange[0]) or (curNum > firstRange[1]):
				if (curNum < secondRange[0]) or (curNum > secondRange[1]):
					print('%d was invalid.' % curNum)
					invalids += 1
		print('invalids:', invalids)
		if invalids >= len(typesDict):
			invalidValues.append(curNum)
			valid = False
			print('%d was invalid.' % curNum)
	if valid:
	  validTickets.append(tick)
			
			
#print(invalidValues)
validTickets.append(fields[1].split('\n')[1])
print(sum(invalidValues))
print(len(otherTickets))
print(len(validTickets))

# 20 in each
matchField = {key: [0 for i in range(20)] for key in typesDict.keys()}
#print(matchField)

for i in range(20):
	for tick in validTickets:
		nums = tick.split(',')
		curNum = int(nums[i])
		for key, ranges in typesDict.items():
			firstRange = ranges[0]
			secondRange = ranges[1]
			'''
			print()
			print('type: %s' % key)
			print(firstRange)
			print(secondRange)
			'''

			if ((curNum < firstRange[0]) or (curNum > firstRange[1])) and ((curNum < secondRange[0]) or (curNum > secondRange[1])):
				continue
			else:
				matchField[key][i] += 1
#print('index %d matches %s' % (i, key))
	
print(matchField)
possibleMatches = {key: [] for key in matchField.keys()}
for key, indices in matchField.items():
	for i in range(20):
		if indices[i] == 191:
			possibleMatches[key].append(i)
'''
unusedIndices = {key: [] for key in matchField.keys()}
for key, indices in possibleMatches.items():
	for i in range(20):
		if i not in indices:
			print('%d is not in %s' % (i, key))
			unusedIndices[key].append(i)
print('unusedIndices')
print(unusedIndices)
	'''
		
for key, item in possibleMatches.items():
	print(key, item)
print()

filterList = [6, 7, 1, 4, 8, 9, 10, 11, 19, 5, 12]
for key, indices in possibleMatches.items():
	for i in filterList:
		if i in indices:
			possibleMatches[key].remove(i)

departureMatches = {}
for key, item in possibleMatches.items():
	print(key, item)
	if 'departure' in key:
		departureMatches[key] = item

print()
print(departureMatches)
for curKey, curItem in departureMatches.items():
	for i in curItem:
		unique = True
		for key, item in possibleMatches.items():
			if key != curKey:
				if i in item:
					unique = False
		if unique:
			print('index %d is unique in %s' % (curItem, curKey))
'''
for i in range(20):
	count = 0
	for key, item in departureMatches.items():
		if i in item:
			count += 1
	if count == 6:
		for key in departureMatches.keys():
			departureMatches[key].remove(i)
'''

matchIndices = [12, 6, 7, 18, 13, 14]
myTicket = fields[1].split('\n')[1]
print(myTicket)
myTicket = myTicket.split(',')
out = 1
for i in range(20):
	if i in matchIndices:
		print('index', i)
		out *= int(myTicket[i])
print(out)
