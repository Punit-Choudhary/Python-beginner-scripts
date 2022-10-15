# ******************** Month Guessing Game ***************************

# Importing library
from datetime import datetime
import random
import time

# Initial Steps to invite in the game:
print("\nWelcome to MONTH GUESSING game by Sachin Dabhade\n")
name = input("Enter your name: ")
print("\nHello " + name.capitalize() + "! Best of Luck!")
time.sleep(1)
print("\nThe game is about to start!\n Let's play and win!\n\n")
time.sleep(1)

# This will record all the activities in my game
def record():
    with open("record.txt", "a") as f:
        f.write(f"The MONTH GUESSING game is played by {name.upper()} on {datetime.now()}\n")
record()

# This will shown after winning
def win():
    print("\nCongratulation...! You won...!")
    print("You are lucky that you did not hanged to the hanger")
    print("   _____ \n"
          "  |     |\n"
          "  |     |\n"
          "  |      \n"
          "  |     O \n"
          "  |    /|\ \n"
          "  |    / \ \n"
          "__|__ -----\n")
    print(
        "\nThanks for playing with us..! We expect you have enjoy our game...!\nSee you again.. Till then take care...!")
    exit()

if __name__ == '__main__':
    # The parameters we require to execute the game:
    words_to_guess = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                      "november", "december"]
    word = random.choice(words_to_guess)
    length = len(word)
    display = '_ ' * length
    limit = 5
    attempt = 0
    score = 0
    
    while limit > attempt:
        guess = input("You have to guess the month of year:" + display + " Enter your guess: \n")
    
        if guess.lower() == word:
            score = score + 1
            win()
    
        else:
            attempt += 1
            print('\n')
            if attempt == 1:
                print("You are going to die...!\n")
                print("  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif attempt == 2:
                print("You are on the way to die...!\n")
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif attempt == 3:
                print("You are few step away to die...!\n")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif attempt == 4:
                print("You are just in front of hanger...!\n")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif attempt == 5:
                print("You are hanged on and you are dead...!\n")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")
                print("Wrong guess. You are hanged!!!\n")
                print("The word was:", word)
    
        print(f"your score is {score} and you have {limit - attempt} chances remaining..!\n\n")
        continue
