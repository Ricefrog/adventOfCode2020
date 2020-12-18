#! /usr/bin/python


def noParensSolve(components):
	while len(components) > 1:
		print('components:', components)
		newComponents = []
		lVal = int(components[0])
		op = components[1]
		rVal = int(components[2])
		if op == '*':
			newComponents.append(lVal * rVal)
		else:
			newComponents.append(lVal + rVal)
		newComponents.extend(components[3:])
		components = newComponents.copy()
	print(components)
	return int(components[0])

def noParensSolve_2(components):
	print('noParensSolve_2')
	print('components:', components)
	while '+' in components and len(components) > 1:
		newComponents = []
		i = components.index('+')
		lVal = int(components[i - 1])
		rVal = int(components[i + 1])
		newComponents.append(lVal + rVal)
		newComponents.extend(components[i + 2:])
		newComponents = components[:i - 1] + newComponents
		components = newComponents.copy()
	print('sending to noParensSolve within 2nd:', components)
	return noParensSolve(components)

def solve_1(components):
	print(components)
	i = 0
	currentStack = []
	while i < len(components):
		if components[i] == '(':
			inParens = []
			matchCount = 1
			while True:
				i += 1
				if components[i] == '(':
					matchCount += 1
					inParens.append(components[i])
				elif components[i] == ')':
					matchCount -= 1
					if matchCount == 0:
						break
					else:
						inParens.append(components[i])
				else:
					inParens.append(components[i])
			i += 1
			currentStack.append(solve_1(inParens))
		else:
			while i < len(components) and components[i] != '(':
				currentStack.append(components[i])
				i += 1
	print('currentStack:')
	print(currentStack)
	return noParensSolve(currentStack)

def solve_2(components):
	print(components)
	i = 0
	currentStack = []
	while i < len(components):
		if components[i] == '(':
			inParens = []
			matchCount = 1
			while True:
				i += 1
				if components[i] == '(':
					matchCount += 1
					inParens.append(components[i])
				elif components[i] == ')':
					matchCount -= 1
					if matchCount == 0:
						break
					else:
						inParens.append(components[i])
				else:
					inParens.append(components[i])
			i += 1
			currentStack.append(solve_2(inParens))
		else:
			while i < len(components) and components[i] != '(':
				currentStack.append(components[i])
				i += 1
	print('currentStack:')
	print(currentStack)
	return noParensSolve_2(currentStack)

inFile = open('input.txt')

lines = inFile.read().split('\n')[:-1]
equationsTemp = [line.split(' ') for line in lines]
equations = []
for equation in equationsTemp:
	temp = []
	for i in range(len(equation)):
		if '(' in equation[i] or ')' in equation[i]:
			for ch in equation[i]:
				temp.append(ch)
		else:
			temp.append(equation[i])
	equations.append(temp)
		
testEquation_1 = ['1', '+', '(', '2', '*', '3', ')', '+', '(', '4', '*', '(', '5', '+', '6', ')', ')']
#solve_1(equations[0])
#solve_1(testEquation_1)

'''
partOneSum = 0
for equation in equations:
	partOneSum += solve_1(equation)
print(partOneSum)
'''

#solve_2(testEquation_1)
partTwoSum = 0
for equation in equations:
	print()
	temp = solve_2(equation)
	print(temp)
	partTwoSum += temp
print(partTwoSum)
