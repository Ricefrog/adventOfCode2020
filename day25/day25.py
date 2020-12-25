#! /usr/bin/python

def get_loop_size(key):
	val = 1
	loops = 0
	subject_number = 7
	while val != key:
		val *= subject_number
		val = val % 20201227
		#print(f'val: {val}')
		loops += 1
	return loops

def transform(loop_size, other_key):
	val = 1
	for i in range(loop_size):
		val *= other_key
		val = val % 20201227
	return val

door_key = 14012298
card_key = 74241
ex_door_key = 17807724
ex_card_key = 5764801
print(get_loop_size(ex_card_key))
print(get_loop_size(ex_door_key))

'''
print(get_loop_size(card_key))
print(get_loop_size(door_key))
'''
print(transform(get_loop_size(door_key), card_key))
