#! /usr/bin/python

inFile = open('input.txt')

lines = inFile.readlines()
originalLines = lines

layer = ['shiny gold']
total = 0
while True:
	nextLayer = []
	newLines = []
	for line in lines:
		desc = line.split()[:2]
		desc = ' '.join(desc)
		if desc == 'shiny gold':
			print(line)
		for item in layer:
			if item in line and desc != item and desc not in nextLayer:
				nextLayer.append(desc)
		if desc not in nextLayer:
			newLines.append(line)
	print()
	print(nextLayer)
	if len(nextLayer) == 0:
		break
	total += len(nextLayer)
	layer = nextLayer
	lines = newLines
print(total)	
print(len(originalLines))

def getLine(descrip, lines):
	for line in lines:
		desc = line.split()[:2]
		desc = ' '.join(desc)
		if desc == descrip:
			return line

def getBags(lines, currentBag):
	currentLine = getLine(currentBag, lines)
	if 'no other bags' in currentLine:
		print('dead end, returning 0')
		return 0
	print(currentLine[:-1])
	bagsContained = {}
	currentTotal = 0
	descs = currentLine.split()[4:]

	for i in range(0, len(descs), 4):
		string = descs[i + 1] + ' ' + descs[i + 2] 
		if descs[i] == 'no':
			descs[i] = 0
		bagsContained[string] = int(descs[i])
	print(bagsContained)
	print()
	for desc, value in bagsContained.items():
		currentTotal += (value + value * getBags(lines, desc))
	print('returning %d' % currentTotal)
	return currentTotal
			

currentBag = 'shiny gold'
lines = originalLines
print(getBags(lines, currentBag))

			
			
		

