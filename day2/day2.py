#! /usr/bin/python

inFile = open('input.txt')
validPasswords = 0
validPasswords_2 = 0

for line in inFile.readlines():
	lower = ''
	upper = ''
	i = 0

	while line[i] != '-':
		lower += line[i]
		i += 1
	i += 1

	while line[i] != ' ':
		upper += line[i]
		i += 1
	i += 1
	lower = int(lower)
	upper = int(upper)

	char = line[i]
	i += 3

	password = line[i:]
	
	numOfChar = password.count(char)

	if numOfChar >= lower and numOfChar <= upper:
		validPasswords += 1
	indexes = 0
	if password[lower - 1] == char:
		indexes += 1
	if password[upper -1] == char:
		indexes += 1
	if indexes == 1:
		validPasswords_2 += 1

#	print('lower: %d, upper: %d, char: %s, pass: %s' % (lower, upper, char, password))
print(validPasswords)
print(validPasswords_2)
