#! /usr/bin/python

inFile = open('input.txt')

def findFirstOutOfOrder(nums, n):
	currentRack = nums[:n]
	print(currentRack)
	for i in range(n, len(nums)):
		possibleSums = []
		for j in range(len(currentRack)):
			for k in range(j + 1, len(currentRack)):
				if currentRack[j] + currentRack[k] not in possibleSums:
					possibleSums.append(currentRack[j] + currentRack[k])
		print()
		print(len(possibleSums))
		print(possibleSums)
		if nums[i] not in possibleSums:
		 	return nums[i]
		currentRack.pop(0)
		currentRack.append(nums[i])
	return 'nothing found.'

def findContiguous(target, nums):
	i = 0
	for i in range(len(nums) - 2):
		contiguous = [nums[i], nums[i + 1]]
		j = i + 2
		while sum(contiguous) <= target:
			if sum(contiguous) == target:
				return contiguous
			else:
				contiguous.append(nums[j])
				j += 1
	return 'nothing found.'
				
		
nums = [int(i) for i in inFile.readlines()]
print(findFirstOutOfOrder(nums, 25))
print(contig := findContiguous(69316178, nums))
contig.sort()
print(contig[0] + contig[-1])

