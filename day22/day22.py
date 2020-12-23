#! /usr/bin/python

import pprint

def recursiveCombat(p1Deck, p2Deck, isSubGame):
	print('p1Deck:', p1Deck)
	print('p2Deck:', p2Deck)
	if not isSubGame:
		print('Original game.')
	#input()
	previousRounds = set()
	while len(p1Deck) > 0 and len(p2Deck) > 0:
		key = (tuple(p1Deck), tuple(p2Deck))
		if key in previousRounds:
			return 'p1'
		else:
			previousRounds.add(key)
		p1Top = p1Deck.pop(0)
		p2Top = p2Deck.pop(0)
		print('Player 1 plays %d!' % p1Top)
		print('Player 2 plays %d!' % p2Top)
		if len(p1Deck) >= p1Top and len(p2Deck) >= p2Top:
			p1DeckCopy = [p1Deck[s] for s in range(p1Top)]
			p2DeckCopy = [p2Deck[s] for s in range(p2Top)]
			print('Entering sub-game.')
			subGameWinner = recursiveCombat(p1DeckCopy, p2DeckCopy, True)
			if subGameWinner == 'p1':
				print('Player 1 wins the round.')
				p1Deck.append(p1Top)
				p1Deck.append(p2Top)
			elif subGameWinner == 'p2':
				print('Player 2 wins the round.')
				p2Deck.append(p2Top)
				p2Deck.append(p1Top)
			else:
				print('Invalid return', subGameWinner)
				return 'error'
		else:
			if p1Top > p2Top:
				print('Player 1 wins the round.')
				p1Deck.append(p1Top)
				p1Deck.append(p2Top)
			else:
				print('Player 2 wins the round.')
				p2Deck.append(p2Top)
				p2Deck.append(p1Top)

	if len(p1Deck) == 0:
		print('Player 2 won.')
		winnerDeck = p2Deck
		if isSubGame:
			print('Player 2 has won a sub-game.')
			#input()
			return 'p2'
	else:
		print('Player 1 won,')
		winnerDeck = p1Deck
		if isSubGame:
			print('Player 1 has won a sub-game.')
			#input()
			return 'p1'
	multiplier = len(winnerDeck)
	score = 0
	for el in winnerDeck:
		print('score: %d, el: %d, multiplier: %d' % (score, el, multiplier))
		score += el * multiplier
		multiplier -= 1
	return score

def part_1(p1Deck, p2Deck):
	while len(p1Deck) > 0 and len(p2Deck) > 0:
		playRound(p1Deck, p2Deck)
		print(p1Deck)
		print(p2Deck)
	if len(p1Deck) == 0:
		winnerDeck = p2Deck
	else:
		winnerDeck = p1Deck
	multiplier = len(winnerDeck)
	score = 0
	for el in winnerDeck:
		print('score: %d, el: %d, multiplier: %d' % (score, el, multiplier))
		score += el * multiplier
		multiplier -= 1
	return score

def playRound(p1Deck, p2Deck):
	p1Top = p1Deck.pop(0)
	p2Top = p2Deck.pop(0)
	print('Player 1 plays %d!' % p1Top)
	print('Player 2 plays %d!' % p2Top)
	if p1Top > p2Top:
		print('Player 1 wins the round.')
		p1Deck.append(p1Top)
		p1Deck.append(p2Top)
	else:
		print('Player 2 wins the round.')
		p2Deck.append(p2Top)
		p2Deck.append(p1Top)
	

inFile = open('input.txt')

temp_1 = inFile.read().split('\n\n')

p1Deck = [int(s) for s in temp_1[0].split('\n')[1:]]
p2Deck = [int(s) for s in temp_1[1].split('\n')[1:-1]]

print(p1Deck)
print(p2Deck)
print(recursiveCombat(p1Deck, p2Deck, False))
#print(part_1(p1Deck, p2Deck))
