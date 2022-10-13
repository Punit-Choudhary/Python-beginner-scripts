# Pyramid Pattern 11
# outer for loop to print the number of rows
# inner for loop to print characters according to
# the given pattern
for i in range(5):
    print(' ' * i, end='')
    for x in range(5 - i):
        print(chr(65 + x), end=' ')
    print()
