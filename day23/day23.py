#! /usr/bin/python
def part_2(cups):
	currentInd = 0
	cupsLen = len(cups)
	for z in range(10000000):
		#print('move %d' % (z + 1))
		currentCup = cups[currentInd]
		pickedUp = []
		pIndex = (currentInd + 1) % cupsLen
		for t in range(3):
			pickedUp.append(cups[pIndex])
			pIndex = (pIndex + 1) % cupsLen

		destCup = currentCup - 1
		if destCup == 0:
			destCup = 1000000
		if destCup in pickedUp:
			while destCup in pickedUp:
				destCup -= 1
				if destCup == 0:
					destCup = 1000000
		for c in pickedUp:
			cups.remove(c)
		destIndex = cups.index(destCup)
		cups = cups[:destIndex + 1] + pickedUp + cups[destIndex + 1:]
		currentInd = (cups.index(currentCup) + 1) % cupsLen

	oneInd = cups.index(1)
	return cups[(oneInd + 1) % cupsLen] * cups[(oneInd + 2) % cupsLen]

def part_1(cups):
	currentInd = 0
	for z in range(100):
		print()
		currentCup = cups[currentInd]
		pickedUp = []
		pIndex = (currentInd + 1) % len(cups)
		for t in range(3):
			pickedUp.append(cups[pIndex])
			pIndex = (pIndex + 1) % len(cups)

		destCup = currentCup - 1
		if destCup == 0:
			destCup = 9
		if destCup in pickedUp:
			while destCup in pickedUp:
				destCup -= 1
				if destCup == 0:
					destCup = 9

		print('\nmove %d' % (z + 1))
		print('cups:', cups)
		print('currentCup:', currentCup)
		print('pickedUp:', pickedUp)
		print('destination:', destCup)
		for c in pickedUp:
			cups.remove(c)
		destIndex = cups.index(destCup)
		cups = cups[:destIndex + 1] + pickedUp + cups[destIndex + 1:]
		currentInd = (cups.index(currentCup) + 1) % (len(cups))

	print('final cups:', cups)
	reordered = []
	ind = cups.index(1) + 1
	for t in range(len(cups) - 1):
		if ind == len(cups):
			ind = 0
		reordered.append(cups[ind])
		ind += 1

	retString = ''
	for c in reordered:
		retString += str(c)
	return retString

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def initializeLoop(input_, nodeDict):
	firstNode = currentNode = Node(input_[0])
	nodeDict[input_[0]] = currentNode

	for v in range(1, len(input_)):
		currentNode.next = Node(input_[v])
		currentNode = currentNode.next
		nodeDict[currentNode.val] = currentNode
	currentNode.next = firstNode
	return firstNode

def printLoop(firstNode):
	currentNode = firstNode
	print('Current value:', currentNode.val)
	print('Next value:', currentNode.next.val)
	print()
	currentNode = currentNode.next
	while currentNode.val != firstNode.val:
		print('Current value:', currentNode.val)
		print('Next value:', currentNode.next.val)
		print()
		currentNode = currentNode.next
	print('Loop end.\n')

def printLoopAsList(firstNode):
	currentNode = firstNode
	print(currentNode.val, end=' ')
	currentNode = currentNode.next
	while currentNode.val != firstNode.val:
		print(currentNode.val, end=' ')
		currentNode = currentNode.next
	print()

def getNode(currentNode, targetVal):
	while currentNode.val != targetVal:
		currentNode = currentNode.next
	return currentNode

def part_1_linked(firstNode, nodeDict):
	currentCup = firstNode
	largestVal = 9

	for z in range(100):
		print('\nmove:', z + 1)
		printLoopAsList(currentCup)
		pickedUpFirst = currentCup.next
		pickedUpLast = pickedUpFirst.next.next
		pickedUpVals = (pickedUpFirst.val, pickedUpFirst.next.val, pickedUpFirst.next.next.val)
		# breakoff loop
		currentCup.next = currentCup.next.next.next.next
		pickedUpLast.next = None
		destinationCupVal = currentCup.val - 1
		if destinationCupVal == 0:
			destinationCupVal = largestVal
		while destinationCupVal in pickedUpVals:
			destinationCupVal -= 1
			if destinationCupVal == 0:
				destinationCupVal = largestVal
		destinationCup = nodeDict[destinationCupVal]
		print('curNext:', currentCup.next.val)
		print('currentCup:', currentCup.val)
		print('pickedUp:', pickedUpVals)
		print('destination:', destinationCup.val)
		pickedUpLast.next = destinationCup.next
		destinationCup.next = pickedUpFirst
		currentCup = currentCup.next
	printLoopAsList(firstNode)

def part_2_linked(firstNode, nodeDict):
	currentCup = firstNode
	largestVal = 1000000

	for z in range(10000000):
		print('move:', z + 1)
		pickedUpFirst = currentCup.next
		pickedUpLast = pickedUpFirst.next.next
		pickedUpVals = (pickedUpFirst.val, pickedUpFirst.next.val, pickedUpFirst.next.next.val)
		# breakoff loop
		currentCup.next = currentCup.next.next.next.next
		pickedUpLast.next = None
		destinationCupVal = currentCup.val - 1
		if destinationCupVal == 0:
			destinationCupVal = largestVal
		while destinationCupVal in pickedUpVals:
			destinationCupVal -= 1
			if destinationCupVal == 0:
				destinationCupVal = largestVal
		destinationCup = nodeDict[destinationCupVal]
		pickedUpLast.next = destinationCup.next
		destinationCup.next = pickedUpFirst
		currentCup = currentCup.next
		
	oneNode = nodeDict[1]
	return oneNode.next.val * oneNode.next.next.val

input_1 = [3, 8, 9, 1, 2, 5, 4, 6, 7]
input_2 = [3, 8, 9, 5, 4, 7, 6, 1, 2]
extraCups = [i for i in range(10, 1000001)]
nodeDict = {}
firstNode = initializeLoop(input_2 + extraCups, nodeDict)
#firstNode = initializeLoop(input_1, nodeDict)
print(part_2_linked(firstNode, nodeDict))
#printLoop(firstNode)
#part_1_linked(firstNode, nodeDict)
#print(part_1(input_1))
#print(part_2(input_2 + extraCups))
