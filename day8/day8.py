#! /usr/bin/python

inFile = open('input.txt')

def execute(lines):
	accValue = 0
	currentIndex = 0
	i = 0
	visitedLines = {i: 0 for i in range(len(lines))}

	while True:
		print('accValue: %d' % accValue)
		if i >= len(lines):
			print('Exiting successfully. accValue = %d' % accValue)
			break
		visitedLines[i] += 1
		if visitedLines[i] > 1:
			print('Revisited line %d.' % i)
			print('accValue = %d' % accValue)
			return False
		instruction, value = lines[i].split()
		print('line %d: %s, %s' % (i, instruction, value))
		if instruction == 'nop':
			i += 1
		elif instruction == 'jmp':
			sign = value[0]
			if sign == '+':
				val = int(value[1:])
			else:
				val = int(value[1:]) * -1
			i += val
		elif instruction == 'acc':
			sign = value[0]
			if sign == '+':
				val = int(value[1:])
			else:
				val = int(value[1:]) * -1
			accValue += val
			i += 1
	return True

def changeInstruction(i, lines):
	instruction, value, = lines[i].split()
	if instruction == 'nop':
		newInstruction = 'jmp'
	elif instruction == 'jmp':
		newInstruction = 'nop'
	print('changing line %d from %s to %s.' % (i, instruction, newInstruction))
	lines[i] = newInstruction + ' ' + value
			
sample1 = ['nop +0',
			'acc +1',
			'jmp +4',
			'acc +3',
			'jmp -3',
			'acc -99',
			'acc +1',
			'jmp -4',
			'acc +6']
execute(sample1)

lines = inFile.readlines()
execute(lines)
originalLines = tuple(lines)

replacable = [i for i in range(len(lines)) if lines[i][:3] == 'nop' or lines[i][:3] == 'jmp']
print(replacable)

for i in replacable:
	lines = list(originalLines)
	changeInstruction(i, lines)
	if execute(lines) == True:
		break
'''
replacable = [i for i in range(len(sample1)) if sample1[i][:3] == 'nop' or sample1[i][:3] == 'jmp']
print(replacable)

originalSample = tuple(sample1)
for i in replacable:
	lines = list(originalSample)
	print(lines)
	changeInstruction(i, lines)
	if execute(lines) == True:
		break
		'''
