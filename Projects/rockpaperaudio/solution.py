 import random
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
engine.say("Enter your name")
engine.runAndWait()
print("Enter your name:",end = ' ')

name = input()
print()
print()
print("Welcome")
engine.say("Welcome")
engine.runAndWait()
print()
print()
count = 1
userPoint = 0
compPoint = 0
while(count <= 10):
    print("Round " + str(count) + " :")
    engine.say("Round " + str(count))
    engine.runAndWait()
    print()
    print("Enter your choice:",end=' ')
    engine.say("Enter your choice:")
    engine.runAndWait()
    user = input()

    if random.randint(1,3) == 1:
        comp = "Rock"
    elif random.randint(1,3) == 2:
        comp = "Paper"
    else:
        comp = "Scissors"
    print("Computer's choice: " + comp)
    engine.say("Computer's choice: " + comp)
    engine.runAndWait()
    count += 1
    if user == "Rock" and comp == "Paper":
        print("Paper beats Rock")
        engine.say("Paper beats Rock")
        engine.runAndWait()
        compPoint += 1
    elif user == "Paper" and comp == "Rock":
        print("Paper beats Rock")
        engine.say("Paper beats Rock")
        engine.runAndWait()
        userPoint += 1
    elif user == "Paper" and comp == "Scissors":
        print("Scissors beats Paper")
        engine.say("Scissors beats Paper")
        engine.runAndWait()
        compPoint += 1
    elif user == "Scissors" and comp == "Paper":
        print("Scissors beats Paper")
        engine.say("Scissors beats Paper")
        engine.runAndWait()
        userPoint += 1
    elif user == "Scissors" and comp == "Rock":
        print("Rock beats Scissors")
        engine.say("Rock beats Scissors")
        engine.runAndWait()
        compPoint += 1
    elif user == "Rock" and comp == "Scissors":
        print("Rock beats Scissors")
        engine.say("Rock beats Scissors")
        engine.runAndWait()
        userPoint += 1
    elif user == comp:
        print("Tie")
        engine.say("Tie")
        engine.runAndWait()
        userPoint += 1
        compPoint += 1
    print()
    print(name + "'s points: " + str(userPoint))
    engine.say(name + "'s points: " + str(userPoint))
    engine.runAndWait()
    print("Computer's points: " + str(compPoint))
    engine.say("Computer's points: " + str(compPoint))
    engine.runAndWait()
    print()
    print()
print()
print()
print()
print("Result:")
engine.say("Result")
engine.runAndWait()
if userPoint > compPoint:
    print(name + " wins") 
    engine.say("Congratulations" + name + "You won the match")
elif compPoint > userPoint:
    print("Computer wins")
    engine.say("Sorry" + name + "Better luck next time")
else:
    print("Match is drawn")   
    engine.say("Match is drawn") 
engine.runAndWait()
