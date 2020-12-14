#! /usr/bin/python

from itertools import permutations

def applyMask(mask, binary):
	newBinary = ''
	for i in range(36):
		if mask[i] == 'X':
			newBinary += binary[i]
		else:
			newBinary += mask[i]
	return newBinary

def createAddresses(preAddress, bitsReplaced, bitsNeeded, decimal, addresses):
	if bitsReplaced == bitsNeeded:
		addresses[preAddress] = decimal
		return
	nextAddress_0 = ''
	nextAddress_1 = ''
	xFound = False
	for i in range(36):
		if not xFound and preAddress[i] == 'X':
			bitsReplaced += 1
			nextAddress_0 += '0'
			nextAddress_1 += '1'
			xFound = True
		else:
			nextAddress_0 += preAddress[i]
			nextAddress_1 += preAddress[i]
	print(nextAddress_0)
	print(nextAddress_1)
	createAddresses(nextAddress_0, bitsReplaced, bitsNeeded, decimal, addresses)
	createAddresses(nextAddress_1, bitsReplaced, bitsNeeded, decimal, addresses)
			


def applyMask_2(mask, binary, decimal, addresses):
	combos = 0
	forCombos = ''
	newBinary = ''
	for i in range(36):
		if mask[i] == 'X':
			newBinary += 'X'
			combos += 1
			forCombos += '0'
			forCombos += '1'
		elif mask[i] == '0':
			newBinary += binary[i]
		else:
			newBinary += '1'
	print()
	print('newBinary:', newBinary)
	print(forCombos)
	createAddresses(newBinary, 0, combos, decimal, addresses)
	'''
	combosLists = set(permutations(forCombos, combos))
#	combosLists = set(combosLists)

	for wilds in combosLists:
		newAddress = ''
		wildInd = 0
		for i in range(36):
			if newBinary[i] != 'X':
				newAddress += newBinary[i]
			else:
				newAddress += wilds[wildInd]
				wildInd += 1
		newAddress = int(newAddress, 2)
		print(newAddress)
		addresses[newAddress] = int(decimal)
		'''
		
	
			

inFile = open('input.txt')

lines_1 = inFile.readlines()
lines = [line[:len(line) - 1] for line in lines_1]

addresses = {}
i = 0
while i <= len(lines):
	if lines[i][:4] == 'mask':
		curMask = lines[i][7:]
		print('curMask', curMask)
		while i < len(lines):
			if i + 1 >= len(lines):
				break
			i += 1
			if lines[i][:4] == 'mask':
				break
			endInd = lines[i].find(']')
			address = lines[i][4:endInd]
			begInd = lines[i].find('=') + 2
			decimal = lines[i][begInd:]
			binary = str(bin(int(decimal)))[2:]
			address_as_bin = str(bin(int(address)))[2:]
			while len(address_as_bin) != 36:
					address_as_bin = '0' + address_as_bin
			while len(binary) != 36:
				binary = '0' + binary
			print('address:', address, 'decimal:', decimal)
			print('binary', binary)
			print('address_as_bin:', address_as_bin)
			applyMask_2(curMask, address_as_bin, int(decimal), addresses)
			'''
			newBinary = applyMask(curMask, binary)
			print('newBinary:', newBinary)
			tempBin = int(newBinary, 2)
			print(tempBin)
			addresses[address] = tempBin
			'''
	else:
		break
'''
part_1 = 0
print(addresses)
for address, val in addresses.items():
	part_1 += val
print(part_1)
'''
part_2 = 0
for address, val in addresses.items():
	part_2 += val
print(part_2)
