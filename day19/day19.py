#! /usr/bin/python

import itertools

def createPossibleMessages_1(rules, ruleNumber, currentPossibilities):
	print()
	print('current rule:', ruleNumber, rules[ruleNumber])
	print('currentPossibilities:', currentPossibilities)
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

	if ruleNumber == 8 or ruleNumber == 11:
		print('ruleNumber:', ruleNumber)
		input()
	if len(rules[ruleNumber]) > 1:
		ruleSet1 = rules[ruleNumber][0]
		ruleSet2 = rules[ruleNumber][1]
		subMsgs_1 = []
		subMsgs_2 = []
		for nextRule in ruleSet1:
			subMsgs_1.append(createPossibleMessages_1(rules, nextRule, currentPossibilities))
		for nextRule in ruleSet2:
			subMsgs_2.append(createPossibleMessages_1(rules, nextRule, currentPossibilities))
		print('subMsgs_1:', subMsgs_1)
		print('subMsgs_2:', subMsgs_2)
		if len(subMsgs_1) == 2:
			subStrings_1 = [a + b for a in subMsgs_1[0] for b in subMsgs_1[1]]
		elif len(subMsgs_1) == 1:
			subStrings_1 = [a for a in subMsgs_1[0]]
		if len(subMsgs_2) == 2:
			subStrings_2 = [a + b for a in subMsgs_2[0] for b in subMsgs_2[1]]
		elif len(subMsgs_2) == 1:
			subStrings_2 = [a for a in subMsgs_2[0]]

		print('subStrings_1:', subStrings_1)
		print('subStrings_2:', subStrings_2)

		tempPoss = currentPossibilities.copy()
		currentPossibilities = [s + b for s in tempPoss for b in subStrings_1]
		currentPossibilities += [s + b for s in tempPoss for b in subStrings_2]
		print('currentPossibilities:', currentPossibilities)
		#input()
		return currentPossibilities
	else:
		subMsgs = []
		for nextRule in rules[ruleNumber][0]:
			print('calling next function with rule %d' % nextRule)
			#input()
			subMsgs.append(createPossibleMessages_1(rules, nextRule, currentPossibilities))
			
		possibleStrings = list(itertools.product(*subMsgs))
		possibleStrings = [''.join(l) for l in possibleStrings]
		print('returned to end loop.')
		print(possibleStrings)
		input()

		return possibleStrings

inFile = open('input.txt')

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
possibilities = ['']
possibleStrings = createPossibleMessages_1(rules, 0, possibilities)
print(possibleStrings)

count = 0
for s in rawMessages:
	if s in possibleStrings:
		count += 1
print(count)
