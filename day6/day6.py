#! /usr/bin/python

inFile = open('input.txt')
'''
currentGroup = []
i = 0
count = 0
for line in inFile.readlines():
	print('i: %d' % i)
	if line == '\n':
		if i == len(inFile.readlines()) - 1:
			for ch in line:
				if ch not in currentGroup and ch != '\n':
					currentGroup.append(ch)
		count += len(currentGroup)
		currentGroup = []
		if i == 2164:
			print('broke')
			break
	else:
		for ch in line:
			if ch not in currentGroup and ch != '\n':
				currentGroup.append(ch)
	print(currentGroup)
	i += 1
currentGroup = []
string = 'wdfkpmalijbncuvrqhnmikpzaygxwsovej'
for ch in string:
	if ch not in currentGroup and ch != '\n': 
		currentGroup.append(ch)
count += len(currentGroup)
print('count: %d' % count)
'''
lines = inFile.readlines()

j = 0
count = 0
while j < len(lines):
	print('j = %d' % j)
	currentGroup = []
	while lines[j] != '\n' and j != len(lines):
		currentGroup.append(lines[j])
		j += 1
		if j == len(lines):
			break
	if len(currentGroup) != 0:
		for ch in currentGroup[0]:
			inEvery = True
			for i in range(1, len(currentGroup)):
				if ch.isalpha() and ch not in currentGroup[i]: 
					print('%s not in %s' % (ch, currentGroup[i]))
					inEvery = False
			if inEvery and ch.isalpha():
				print('at index %d all yes for %s' % (j, ch))
				count += 1
	j += 1

print(count)


