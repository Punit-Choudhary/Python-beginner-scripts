# the following code will give us the required pattern
# incresing sizeofpattern will increase the size

sizeofpattern = 5
for i in range(sizeofpattern):
    if i == 0:
        print("* "*sizeofpattern)
    elif i == sizeofpattern-1:
        for i in range(sizeofpattern//2):
            print('*', end=' ')
    else:
        print(" "*(sizeofpattern-1)+"*")
