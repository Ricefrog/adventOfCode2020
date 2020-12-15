#! /usr/bin/python

def part_1(firstNumbers):
	turn = 1
	#  number: [new/old, turnSpoken, turnBeforeThat]
	numbersSpoken = {}
	for num in firstNumbers:
		numbersSpoken[num] = ['new', turn, 0]
		turn += 1

	lastSpoken = firstNumbers[-1]
	print('initially:', numbersSpoken)
	print('lastSpoken:', lastSpoken)

	while turn < 30000001:
		print()
		print('turn', turn, ' lastSpoken', lastSpoken, end='')
		if numbersSpoken[lastSpoken][0] == 'new':
			previousTurn = numbersSpoken[0][1]
			numbersSpoken[0] = ['old', turn, previousTurn]
			print(' spoken: 0')
			lastSpoken = 0
			turn += 1
		else:
			age = numbersSpoken[lastSpoken][1] - numbersSpoken[lastSpoken][2]
			if age not in numbersSpoken:
				numbersSpoken[age] = ['new', turn, 0]
			else:
				previousTurn = numbersSpoken[age][1]
				numbersSpoken[age] = ['old', turn, previousTurn]
#print(' spoken: ', age)
			lastSpoken = age
			turn += 1
#print(numbersSpoken)
	print('turn:', turn)

	for val, keyList in numbersSpoken.items():
		if keyList[1] == 30000000:
#print(numbersSpoken[val])
			return val


sampleInput = [0, 3, 6]
sampleInput2 = [1, 0, 18, 10, 19, 6]
print(part_1(sampleInput2))
