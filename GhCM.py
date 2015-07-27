#!/usr/bin/env python

import os
import sys
import uuid
from datetime import date, datetime, time, timedelta 
from random import randint
import git
import click

letters = [ 
	[ 0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0 ], 
	[ 1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0 ], 
	[ 1,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,1,1,1,1,1 ]
]

board = [ [0] * 52, [0] * 52, [0] * 52, [0] * 52, [0] * 52, [0] * 52, [0] * 52 ]

@click.command()
@click.argument('message', nargs=1)
@click.option('--textColor', default=4, type=click.IntRange(0,4), help='Changes color of text, 0 = lightest | 4 = darkest.')
@click.option('--backgroundColor', default=0, type=click.IntRange(0,4), help='Changes color of background, 0 = lightest | 4 = darkest.')

def main(message, textcolor, backgroundcolor):
	if len(message) > 8:
		print "ERROR: Message too long, must be <= 8 characters"
		sys.exit()

	if not message.isalpha():
		print "ERROR: Message must contain only letters"
		sys.exit()

	offset = 1
	for character in message.lower():
		copyLetter(ord(character)  - 97, offset)
		offset += 6
	makeCommits(message, textcolor, backgroundcolor)

	print "\nFinished. Push the folder 'GhCM - " + message + "' to a repo on your GitHub to have your message appear."

def copyLetter(position, offset):
	for i in range(7):
		for j in range(5):
			board[i][j + offset] = letters[i][j + (position * 5)]

def makeCommits(message, textColor, backgroundColor):
	if not os.path.exists("GhCM - " + message):
		os.makedirs("GhCM - " + message)

	repo = git.Repo.init(os.path.join(os.getcwd(), "GhCM - " + message))

	currentDate = date.today() - timedelta(((date.today().weekday() + 1) % 7) + 1)
	
	for j in range(50, -1, -1):
		for i in range(6, -1, -1):
			if board[i][j]:
				for i in range(textColor):
					commit_date = datetime.combine(currentDate, time(hour=randint(0, 23), minute=randint(0, 59), second=randint(0, 59), microsecond=randint(0, 999999))).strftime("%Y-%m-%d %H:%M:%S")
					repo.index.add([createRandomFile(message)])
					repo.index.commit(str(uuid.uuid1()), author_date=commit_date, commit_date=commit_date)
			else:
				for i in range(backgroundColor):
					commit_date = datetime.combine(currentDate, time(hour=randint(0, 23), minute=randint(0, 59), second=randint(0, 59), microsecond=randint(0, 999999))).strftime("%Y-%m-%d %H:%M:%S")
					repo.index.add([createRandomFile(message)])
					repo.index.commit(str(uuid.uuid1()), author_date=commit_date, commit_date=commit_date)
			
			currentDate = currentDate - timedelta(1)

def createRandomFile(message):
	with open('GhCM - ' + message + '/file.txt', 'w') as f:
		f.write(str(uuid.uuid1()))
	return 'file.txt'

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


