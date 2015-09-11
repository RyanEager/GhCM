#!/usr/bin/env python

import os
import sys
import uuid

from datetime import date, datetime, time, timedelta 
from random import randint

import click
import git


letters = [ 
	[ 0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0 ], 
	[ 1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0 ], 
	[ 1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0 ], 
	[ 1,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,1,1,1,1,1 ]
]

board = [ 
	[0] * 52, 
	[0] * 52, 
	[0] * 52, 
	[0] * 52, 
	[0] * 52, 
	[0] * 52, 
	[0] * 52 
]

# set up commandline
@click.command()
@click.argument('message', nargs=1)
@click.option('--textColor', default=2, type=click.IntRange(0,4), help='Changes color of text, 0 = lightest | 4 = darkest.')
@click.option('--backgroundColor', default=0, type=click.IntRange(0,4), help='Changes color of background, 0 = lightest | 4 = darkest.')


def main(message, textcolor, backgroundcolor):
	if len(message) > 8:
		print "ERROR: Message too long, must be <= 8 characters"
		sys.exit()

	if not message.isalpha():
		print "ERROR: Message must contain only letters"
		sys.exit()

	print"Creating Repo..."

	offset = 1
	for character in message.lower():
		copyLetter(ord(character)  - 97, offset)
		offset += 6

	makeCommits(message, textcolor, backgroundcolor)

	print "Finished. \nPush the folder 'GhCM - " + message + "' to a repo on your GitHub to have your message appear."



def copyLetter(position, offset):
	for row in range(7):
		for col in range(5):
			board[row][col + offset] = letters[row][col + (position * 5)]


def makeCommits(message, textColor, backgroundColor):
	# create folder for the repo
	if not os.path.exists("GhCM - " + message):
		os.makedirs("GhCM - " + message)

	# create the repo
	repo = git.Repo.init(os.path.join(os.getcwd(), "GhCM - " + message))

	# set the start date to the last full col in on the graph
	currentDate = date.today() - timedelta(((date.today().weekday() + 1) % 7) + 1)

	# make commits for each cell of the board
	# stepping from bottom right and passing through each col from bottom to top
	for col in range(50, -1, -1):
		for row in range(6, -1, -1):

			color = backgroundColor

			if board[row][col]:
				color = textColor

			for i in range(color):
					commit_date = datetime.combine(currentDate, time(hour=randint(0, 23), minute=randint(0, 59), second=randint(0, 59))).strftime("%Y-%m-%d %H:%M:%S")
					repo.index.add([createRandomFile(message)])
					repo.index.commit(str(uuid.uuid1()), author_date=commit_date, commit_date=commit_date)
			
			currentDate = currentDate - timedelta(1)


def createRandomFile(message):
	with open('GhCM - ' + message + '/file.txt', 'w') as f:
		f.write(str(uuid.uuid1()))
	return 'file.txt'


def printBoard():
	for row in range(7):
		for col in range(52):
			 if board[row][col] == 1:
			 	print 1,
			 else:
			 	print " ",
		print ""


if __name__ == '__main__':
	main()
