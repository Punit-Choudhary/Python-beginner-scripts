x = int(input())
for y in range(1, x+1):
    for i in range(y, y+x):
        print(i, end=' ')
    print('\n')
