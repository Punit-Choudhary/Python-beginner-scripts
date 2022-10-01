import requests
import sys

wordlist = input("Enter path to file: ")
sublist = open(wordlist).read()
dirs = sublist.splitlines()

for dir in dirs:
    direnum = f"http://{sys.argv[1]}/{dir}"
    r = requests.get(direnum)
    if r.status_code == 404:
        pass
    else:
        print("Valid dir: ", direnum)
