# -*- coding: utf-8 -*-
# GAME

# THE BALL IS IN WHICH GLASS?

from random import shuffle
import time
from os import system, name


# For clearing screen

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# shuffling list

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


cup = [' ', '0', ' ']


# input as player's guess of ball in a glass
# player enters postion of glass (index of list)

def player_guess():
    guess = ' '
    while guess not in ['0', '1', '2']:
        guess = input('\nPick a glass: 0,1,2 -->')
        clear()
    return int(guess)


#Checking whether guess is correct or not

def check_guess(cup, guess):
    if cup[guess] == '0':
        print( """
CONGRATULATIONS
Correct Guess!!
***You Won!!***
""")
    else:
        print ('wrong input', cup)


# initial list

ball = [' ', '0', ' ']

while 1:
    print ('\nSee the ball in the glass-->', ball)
    time.sleep(0.5)
    print( '\nNow shuffling glasses...')
    shuffle(ball)
    time.sleep(0.5)
    print ('''
--Glasses shuffled--
''')
    time.sleep(0.5)

    print( """Choose:
    1. Play
    2. Exit game""")

    choice = int(input('Enter choice:'))
    if choice == 1:
        guess = player_guess()
        check_guess(ball, guess)
    elif choice == 2:
        print( '''
***GAME ENDED***
''')
        exit(1)
    time.sleep(1)
    clear()
