# alpahbetic pattern 101
for i in range(5):
    print('-'*(4-i), end='-')
    for x in range(2*i+1):
        if x == 0 or x == 2*i:
            print('*', end='')
        else:
            print('-', end='')
    print('-'*(4-i), end='-')
    print()
