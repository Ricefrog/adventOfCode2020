#! /usr/bin/python

def part_1(allergensDict, ingredientsList):
	'''
	for allergen, items in allergensDict.items():
		for ingredients in ingredientsList:
			if allergen not in ingredients:
				for ing in ingredients:
					if ing in items:
						allergensDict[allergen].remove(ing)
	print(allergensDict)
	'''
	for allergen, items in allergensDict.items():
		for ingredients in ingredientsList:
			print('checking:', ingredients)
			if allergen in ingredients:
				for ing in items:
					if ing not in ingredients:
						print('%s cannot be %s' % (ing, allergen))
						allergensDict[allergen] = [s for s in allergensDict[allergen] if s != ing]
	print(allergensDict)

	nonAllergens = []
	count = 0
	for ingredients in ingredientsList:
		for ing in ingredients:
			found = False
			if ing in allergensDict.keys():
				continue
			for allergen, items in allergensDict.items():
				if ing in items:
					found = True
					break
			if not found:
				nonAllergens.append(ing)
				count += 1
	print(nonAllergens)
	return count
		
				
				
			

inFile = open('input.txt')

allergensDict = {}
ingredientsList = []
for line in inFile.read().split('\n'):
	parenInd = line.find('(')
	tempList = line[:parenInd].split(' ')
	if '' in tempList:
		tempList.remove('')
	if len(tempList) > 0:
		containsChunk = line[parenInd + 10:-1]
		print('countainsChunk:', containsChunk)
		if len(containsChunk) == 1:
			if containsChunk in allergensDict:
				allergensDict[containsChunk] += tempList
			else:
				allergensDict[containsChunk] = tempList
			ingredientsList.append(tempList + containsChunk)
		else:
			tempList_2 = []
			for al in containsChunk.split(','):
				if al.strip() in allergensDict:
					allergensDict[al.strip()] += tempList
				else:
					allergensDict[al.strip()] = tempList
				tempList_2.append(al.strip())
			ingredientsList.append(tempList + tempList_2)

print(ingredientsList)
print(allergensDict)
'''
for key, items in allergensDict.items():
	allergensDict[key] = list(set(items))
print(allergensDict)
'''
for key in allergensDict.keys():
	print(key)
input()
print()
print(part_1(allergensDict, ingredientsList))
# part 2
for key, items in allergensDict.items():
	allergensDict[key] = list(set(items))
print(allergensDict)

filtered = []
i = 0
while i < 2000:
	for key, items in allergensDict.items():
		if len(items) == 1 and items[0] not in filtered:
			filterAllergen = items[0]
			filtered.append(filterAllergen)
			for oKey, oItems in allergensDict.items():
				if oKey != key:
					allergensDict[oKey] = [s for s in oItems if s != filterAllergen]
	i += 1
print(allergensDict)
filtered = []
for key in sorted(list(allergensDict.keys())):
	filtered.append(allergensDict[key][0])
print(','.join(filtered))
