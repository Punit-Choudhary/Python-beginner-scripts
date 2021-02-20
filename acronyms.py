#!python3
# acronyms.py - Create acronyms(short form of word)

user_input = input("Enter a Phrase: ")
text = user_input.split()

acronyms = " "

for i in text:
	acronyms += str(i[0].upper())

print(f"Acronyms of '{user_input}' is {acronyms}")
