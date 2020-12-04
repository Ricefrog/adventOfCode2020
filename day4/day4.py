#! /usr/bin/python

def validate(field, info):
	if field == 'byr':
		if int(info) < 1920 or int(info) > 2002:
			return False
	elif field == 'iyr':
		if int(info) < 2010 or int(info) > 2020:
			return False
	elif field == 'eyr':
		if int(info) < 2020 or int(info) > 2030:
			return False
	elif field == 'hgt':
		mes = ''
		if not info.find('cm') == -1:
			mes += 'cm'
		if not info.find('in') == -1:
			mes += 'in'
		if mes != 'in' and mes != 'cm':
			return False
		justInts = [ch for ch in info if ch.isdigit()]
		year = int(''.join(justInts))
		if mes == 'in':
			if year < 59 or year > 76:
				return False
		else:
			if year < 150 or year > 193:
				return False
	elif field == 'hcl':
		allowed = '0123456789abcedf'
		if len(info) != 7:
			return False
		if info[0] != '#':
			return False
		for ch in info[1:]:
			if ch not in allowed:
				return False
	elif field == 'ecl':
		allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		if info not in allowed:
			return False
	elif field == 'pid':
		if not info.isdecimal():
			return False
		if len(info) != 9:
			return False
	return True
			
			
		
		

inFile = open('input.txt')

validPassports = 0
currentPass = {}
lines = inFile.readlines()
index = 0
numOfPassports = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for i in range(len(lines)): 
	if index >= len(lines) -1:
		break
	if lines[index] == '\n':
		#evaluate passport	
		numOfPassports += 1
		print('checking pass number %d at index %d' % (numOfPassports, index))
		print(currentPass)
		passes = True
		for field in fields:
			print('checking field %s' % field)
			if field not in currentPass.keys():
				print('this field was not found')
				passes = False
				break
			else:
				passes = validate(field, currentPass[field])
				if passes == False:
					break
		if passes == True:
			print('this passport passed.')
			validPassports += 1
		else: 
			print('this passport did not pass')
		currentPass = {}
	else:
		print('currentLine: %s' % lines[index])
		while lines[index] != '\n':
			curFields = lines[index].split()
			for string in curFields:
				end = string.find(':')
				field = string[:end]
				info = string[end + 1:]
				print('adding field %s' % field)
				currentPass[field] = info
			index += 1
			if index >= len(lines):
				break
		index -= 1
	index += 1
print(validPassports)
		
		
