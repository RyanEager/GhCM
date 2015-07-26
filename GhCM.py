#!/usr/bin/env python

import os
import sys
import uuid
from datetime import date, datetime, time, timedelta 
from random import randint
import git

letters = [ 
	[ 0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0 ], 
	[ 1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0 ], 
	[ 1,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,1,1,1,1,1 ]
]

board = [ [0] * 52, [0] * 52, [0] * 52, [0] * 52, [0] * 52, [0] * 52, [0] * 52 ]

def main():
	if len(sys.argv) != 2 :
		print "\nUsage: GhCM.py <message>"
		sys.exit()

	if len(sys.argv[1]) > 8:
		print "ERROR: Message too long, must be <= 8 characters"
		sys.exit()

	if not sys.argv[1].isalpha():
		print "ERROR: Message must contain only letters"
		sys.exit()

	offset = 1
	for character in sys.argv[1].lower():
		copyLetter(ord(character)  - 97, offset)
		offset += 6
	makeCommits()

def copyLetter(position, offset):
	for i in range(7):
		for j in range(5):
			board[i][j + offset] = letters[i][j + (position * 5)]

def makeCommits():
	if not os.path.exists("GhCM - " + sys.argv[1]):
		os.makedirs("GhCM - " + sys.argv[1])

	repo = git.Repo.init(os.path.join(os.getcwd(), "GhCM - " + sys.argv[1]))

	currentDate = date.today() - timedelta(((date.today().weekday() + 1) % 7) + 1)
	
	for j in range(50, -1, -1):
		for i in range(6, -1, -1):
			if board[i][j]:
				for i in range(4):
					commit_date = datetime.combine(currentDate, time(hour=randint(0, 23), minute=randint(0, 59), second=randint(0, 59), microsecond=randint(0, 999999))).strftime("%Y-%m-%d %H:%M:%S")
					
					repo.index.add([createRandomFile()])
					repo.index.commit(str(uuid.uuid1()), author_date=commit_date, commit_date=commit_date)
			currentDate = currentDate - timedelta(1)

def createRandomFile():
	with open('GhCM - ' + sys.argv[1] + '/main.c', 'w') as f:
		f.write(str(uuid.uuid1()))
	return 'main.c'

def printBoard():
	for i in range(7):
		for j in range(52):
			 if board[i][j] == 1:
			 	print 1,
			 else:
			 	print " ",
		print ""

if __name__ == '__main__':
	main()