#! /usr/bin/python

import requests, os, pyperclip

url = pyperclip.paste()
print('url is taken from the clipboard.')
print('target url: %s' % url)
print('Is this the url you want to use? (y or n): ', end='')
userSelection = input()
if userSelection == 'y':
	res = requests.get(url)
	res.raise_for_status()
	print('url is valid.')
	print('Enter the filepath: ', end='')
	path = input()
	if not os.path.exists(os.path.split(path)[0]):
		print('Path is not valid: %s' % path)
	elif path[len(path) - 4:] != '.txt':
		print('Path entered: %s' % path)
		print('This program will only write to .txt files.')
		print('The path entered ends with %s' % path[len(path) - 4:])
	else:
		testTxt = open(path, 'wb')
		for chunk in res.iter_content(100000):
			testTxt.write(chunk)
		print('Test case has been written to %s' % path)
else:
	print('Exiting program.')
