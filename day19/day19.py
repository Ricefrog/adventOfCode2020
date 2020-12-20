#! /usr/bin/python

import itertools

def createPossibleMessages_1(rules, ruleNumber, currentPossibilities, layer, maxLayer):
	print()
	print('current rule:', ruleNumber, rules[ruleNumber])
	#print('currentPossibilities:', currentPossibilities)
	if rules[ruleNumber] == 'a':
		retPossibilities = []
		for sub in currentPossibilities.copy():
			retPossibilities.append(sub + 'a')
		return retPossibilities
	if rules[ruleNumber] == 'b':
		retPossibilities = []
		for sub in currentPossibilities.copy():
			retPossibilities.append(sub + 'b')
		return retPossibilities

	if ruleNumber == 8 or ruleNumber == 11 or ruleNumber == 42 or ruleNumber == 31:
		print('ruleNumber:', ruleNumber)
		print('layer:', layer)
		#input()
		if layer == maxLayer:
			return ['']

	if len(rules[ruleNumber]) > 1:
		ruleSet1 = rules[ruleNumber][0]
		ruleSet2 = rules[ruleNumber][1]
		subMsgs_1 = []
		subMsgs_2 = []
		for nextRule in ruleSet1:
			subMsgs_1.append(createPossibleMessages_1(rules, nextRule, currentPossibilities, layer + 1, maxLayer))
		for nextRule in ruleSet2:
			subMsgs_2.append(createPossibleMessages_1(rules, nextRule, currentPossibilities, layer + 1, maxLayer))
		#print('subMsgs_1:', subMsgs_1)
		#print('subMsgs_2:', subMsgs_2)
		if ruleNumber == 8 or ruleNumber == 11 or ruleNumber == 42 or ruleNumber == 31:
			print('ruleNumber:', ruleNumber)
			#input()
		subStrings_1 = ['']
		subStrings_2 = ['']
		if len(subMsgs_1) == 2:
			subStrings_1 = [a + b for a in subMsgs_1[0] for b in subMsgs_1[1]]
		elif len(subMsgs_1) == 1:
			subStrings_1 = [a for a in subMsgs_1[0]]

		if len(subMsgs_2) == 2:
			subStrings_2 = [a + b for a in subMsgs_2[0] for b in subMsgs_2[1]]
		elif len(subMsgs_2) == 1:
			subStrings_2 = [a for a in subMsgs_2[0]]

		#print('subStrings_1:', subStrings_1)
		#print('subStrings_2:', subStrings_2)

		tempPoss = currentPossibilities.copy()
		currentPossibilities = [s + b for s in tempPoss for b in subStrings_1]
		currentPossibilities += [s + b for s in tempPoss for b in subStrings_2]
		#print('currentPossibilities:', currentPossibilities)
		#input()
		return currentPossibilities
	else:
		subMsgs = []
		for nextRule in rules[ruleNumber][0]:
			print('calling next function with rule %d' % nextRule)
			#input()
			subMsgs.append(createPossibleMessages_1(rules, nextRule, currentPossibilities, layer + 1, maxLayer))
			
		if layer == 0:
			#print(subMsgs)
			print('lists in subMsgs:', len(subMsgs))
			print('length of first list:', len(subMsgs[0]))
			print('length of second list:', len(subMsgs[1]))
			subMsgs[0] = list(set(subMsgs[0]))
			print('length of first list after removing copies:', len(subMsgs[0]))
			return subMsgs
		possibleStrings = itertools.product(*subMsgs)
		possibleStrings = [''.join(l) for l in possibleStrings]

		return possibleStrings

inFile = open('input3.txt')

lines = inFile.read().split('\n\n')
rawRules = lines[0].split('\n')
rawMessages = lines[1].split('\n')[:-1]
print(rawRules)
print(rawMessages)	

part_2 = True
rules = {}
for rule in rawRules:
	if part_2:
		if rule == '8: 42':
			print('rule was changed.')
			input()
			rule = '8: 42 | 42 8'
		elif rule == '11: 42 31':
			print('rule was changed.')
			input()
			rule = '11: 42 31 | 42 11 31'
	colInd = rule.find(':')
	key = int(rule[:colInd])
	if 'a' in rule:
		rules[key] = 'a'
	elif 'b' in rule:
		rules[key] = 'b'
	elif '|' in rule:
		print('rule:', rule)
		temp = rule[colInd + 2:]
		left, right = temp.split('|')
		left = left.split(' ')
		right = right.split(' ')
		if '' in left:
			left.remove('')
		if '' in right:
			right.remove('')
		lRules = [int(l) for l in left]
		rRules = [int(l) for l in right]
		rules[key] = [lRules, rRules]
	else:
		temp = rule[colInd + 2:]
		rules[key] = [[int(l) for l in temp.split(' ')]]
print(rules)
largestMsg = 0
for msg in rawMessages:
	if len(msg) > largestMsg:
		largestMsg = len(msg)
possibilities = ['']
'''
# for part 1
possibleStrings = createPossibleMessages_1(rules, 0, possibilities, 0, 7)
#print(possibleStrings)
largestResult = 0
for msg in possibleStrings:
	if len(msg) > largestResult:
		largestResult = len(msg)
print('largestMsg: %d, largestResult: %d' % (largestMsg, largestResult))

count = 0
for s in rawMessages:
	if s in possibleStrings:
		count += 1
print(count)
'''

count = 0
matchingStrings = []
for i in range(2, 10):
	subMsgs = createPossibleMessages_1(rules, 0, possibilities, 0, i)
	print('i:', i)
	sub_1_length = len(subMsgs[0][0])
	sub_2_length = len(subMsgs[1][0])
	print('s1len:', sub_1_length, 's2len:', sub_2_length)
	print('largestMsg: %d, largestResult: %d' % (largestMsg, sub_1_length + sub_2_length))
	if sub_1_length + sub_2_length >= largestMsg:
		break
	for s in rawMessages.copy():
		if len(s) == sub_1_length + sub_2_length:
			s_1 = s[:sub_1_length]
			s_2 = s[sub_1_length:]
			print('s_1:', s_1)
			print('s_2:', s_2)
			if s_1 in subMsgs[0] and s_2 in subMsgs[1]:
				matchingStrings.append(s)
				rawMessages.remove(s)
				count += 1
	print('count:', count)
	input()
print(matchingStrings)
