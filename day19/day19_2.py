#! /usr/bin/python

rules, tests = open('input.txt').read().strip().split('\n\n')

dr = {}
for r in rules.split('\n'):
	rn, val = r.split(': ')
	if int(rn) == 8:
		val =  '42 | 42 8'
	if int(rn) == 11:
		val = '42 31 | 42 11 31'
	dr[int(rn)] = val

def consume(x, rn):
	print('x:', x, 'rn:', rn)
	rule = dr[rn]
	if rule[0] == '"': # this is a or b
		rule = rule.strip('"')
		if x.startswith(rule):
			return [len(rule)]
		else:
			return []
	bret = []
	for opt in rule.split(' | '):
		acc = [0]
		for rn in opt.split(' '):
			nacc = []
			rn = int(rn)
			for ac in acc:
				ret = consume(x[ac:], rn)
				for c in ret:
					nacc.append(c + ac)
			acc = nacc
		bret += acc
	return bret

acc = 0
for x in tests.split('\n'):
	acc += len(x) in consume(x, 0) 
print(acc)
