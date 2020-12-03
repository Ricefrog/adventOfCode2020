#! /usr/bin/python

inFile = open('input.txt')
nums = []
for line in inFile.readlines():
	nums.append(int(line))
a = 0
b = 0
for i in range(len(nums)):
	a = nums[i]
	for j in range(len(nums)):
		if j == i:
			continue
		b = nums[j]
		if a + b == 2020:
			solution = [a, b, a * b]
# Part two
a = 0
b = 0
c = 0
sums = [[i, j, k, i + j + k] for i in nums for j in nums for k in nums]
for curList in sums:
	if curList[3] == 2020:
		print(curList)
		prod = curList[0] * curList[1] * curList[2]	
		solution = [curList[0], curList[1], curList[2], prod]
print(solution)
