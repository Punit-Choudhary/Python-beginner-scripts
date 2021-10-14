#GAME

#THE BALL IS IN WHICH GLASS?

from random import shuffle
import time
from os import system,name

# For clearing screen
def clear():
    if name=='nt':
        _=system('cls')
    else:
        _=system('clear')

#shuffling list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

cup=[" ","0"," "]

#input as player's guess of ball in a glass
#player enters postion of glass (index of list)
def player_guess():
    guess=" "
    while guess not in ['0','1','2']:
        guess=input("\nPick a glass: 0,1,2 -->")
        clear()
    return int(guess)

def check_guess(cup,guess):
    if cup[guess]=='0':
        print("\nCONGRATULATIONS\nCorrect Guess!!\n***You Won!!***\n")
    else:
        print("wrong input",cup)

#initial list
ball=[' ','0',' ']

while 1:
    print("\nSee the ball in the glass-->",ball)
    time.sleep(1)
    print("\nNow shuffling glasses...")
    shuffle(ball)
    time.sleep(1)
    print("\n--Glasses shuffled--\n")
    time.sleep(1)

    print("""Choose:
    1. Play
    2. Exit game""")

    choice=int(input("Enter choice:"))
    if choice==1:
        guess=player_guess()
        check_guess(ball,guess)
    elif choice==2:
        print("\n***GAME ENDED***\n")
        exit(1)
    time.sleep(3)
    clear()


