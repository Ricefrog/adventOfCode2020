#! /usr/bin/python

from collections import defaultdict

inFile = open('input.txt')

chains = []
def possibilities(adapters, index, currentChain):
	if index == len(adapters) - 1:
		if currentChain not in chains:
			chains.append(currentChain)
		return 
	curJoltage = adapters[index]
	i = index + 1
	while i <= len(adapters) - 1 and adapters[i] <= curJoltage + 3:
		nextChain = currentChain + [adapters[i]]
		possibilities(adapters, i, nextChain)
		i += 1
	

lines = inFile.readlines()
adapters = [int(i) for i in lines]
adapters.sort()
print(adapters)

lastJoltage = adapters[len(adapters) - 1] + 3
print(lastJoltage)
adapters.append(lastJoltage)
adapters = [0] + adapters
print(adapters)
jolts = {1: 0, 2: 0, 3: 0}

for i in range(1, len(adapters)):
	jolts[adapters[i] - adapters[i -1]] += 1
print(jolts)
print()

'''
possibilities = 1
for i in range(len(adapters)):
	print('adapters[%d]: %d' % (i, adapters[i]))
	curJoltage = adapters[i]
	nextPositions = 0
	j = i + 1
	while j <= len(adapters) - 1 and adapters[j] <= curJoltage + 3:
		nextPositions += 1
		j += 1
	print('nextPositions = %d' % nextPositions)
	possibilities *= nextPositions
	print('possibilities: %d' % possibilities)
print(possibilities)
'''

'''
possibilities(adapters, 0, [0])
print(len(chains))
'''

dp = defaultdict(int)
dp[0] = 1
for x in adapters[1:-1]:
	dp[x] += dp[x - 1] + dp[x - 2] + dp[x - 3]
print(dp)
print(sum(dp.values()))
