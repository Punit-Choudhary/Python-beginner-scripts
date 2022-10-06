from time import sleep
from random import choice
from colorama import init
from colorama import Fore, Style

charset = 'abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
cs2 = '!@#$%^&*()`~-_=+\\|]}[{\"\';:/.>,<?'
cs = []

init()

e = [Style.DIM, Style.BRIGHT, Style.NORMAL]
for c in charset:
    cs.append(c)
    print(Fore.GREEN)

while True:
    sleep(.001)
    print(choice(e)+choice(cs), flush=True, end='')
