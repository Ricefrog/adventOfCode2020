#! /usr/bin/python

inFile = open('input.txt')

rows = []

for line in inFile.readlines():
	currentRow = []
	for ch in line:
		if ch == '.':
			currentRow.append(0)
		else:
			currentRow.append(1)
	rows.append(currentRow)

for i in range(10):
	print(rows[i])

numberOfRows = len(rows)
rowWidth = len(rows[0])
horizontalDistance = 3 * numberOfRows
print('numberOfRows: %d, rowWidth: %d' % (numberOfRows, rowWidth))
print('horizontalDistance: %d' % horizontalDistance)

verticalTravelled, horizontalTravelled = 0, 0
trees = 0
trees2 = 0
for i in range(len(rows)):
	print('i: %d' % i)
	row = rows[i]
	index = horizontalTravelled % (rowWidth	- 1)
	print('index: %d' % index)
	if row[index] == 1:
		trees += 1
		print('hit')
	horizontalTravelled += 3

print('*' * 20)
horizontalTravelled = 0
for i in range(len(rows)):
	if i % 2 != 0:
		continue
	print('i: %d' % i)
	row = rows[i]
	index = horizontalTravelled % (rowWidth	- 1)
	print('index: %d' % index)
	if row[index] == 1:
		trees2 += 1
		print('hit')
		print(row)
	horizontalTravelled += 1
print(trees)
print(trees2)
		
