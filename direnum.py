import requests
import sys

sublist = open('wordlist2.txt').read()
dirs = sublist.splitlines()

for dir in dirs:
    direnum = f"http://{sys.argv[1]}/{dir}"
    r = requests.get(direnum)
    if r.status_code == 404:
        pass
    else:
        print("Valid dir: ", direnum)