#!/usr/bin/python3
#The purpose of this program is to take a list of throws from a bowling game(in the form of a string) and then convert it to a accurate bowling score.
#By: Jordan Hair
#Date: August 19th 2018


import sys 
frame = 0          #frame counter 
throw = 0          #throw flag
score = 0 	   #final score 
i = 0  	 	   #interator

def trans(key,tempi):
	dic = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '-':0, 'X':10}
	if (key == '/'): #spare value eval
		return (10 - dic[game[tempi-1]])
	else:
		return dic[key]
try:
	game = sys.argv[1] #input string 
	while (frame < 10): #do for 10 frames
		turn = game[i]
		if turn == 'X': #strike
			frame += 1 #frame complete 
			throw = 0 
			score += 10 + trans(game[i+1], i+1) + trans(game[i+2], i+2) #add next and next next rolls
		elif turn == '/':
			frame += 1 #frame complete 
			throw = 0 #throw reset 
			score += trans(game[i],i) + trans(game[i+1], i+1) #add next roll
		elif turn == '-':
			if throw : #fame complete 
				frame += 1 
				throw = 0 
			else: #first throw 
				throw = 1
		elif turn.isdigit():
			score += trans(game[i], i) 
			if throw: #fame complete 
				frame += 1 
				throw = 0
			else: #first throw 
				throw = 1 
		elif turn.isdigit():
			score += trans(game[i], i)
			if throw: #fame complete 
				frame += 1 
				throw = 0 
			else: #first throw 
				throw = 1
		i += 1
except:
	print('String provided is invalid, or incorrect amount of throws.\nPlease try again.\nExiting...')
	exit()
print(score)
