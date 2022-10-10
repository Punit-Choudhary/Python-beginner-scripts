# pyramid pattern 10
# We use the outer for loop to print rows.
# and inner for loop to rint columns.
# Each line of this pattern has some spaces and some characters
# The sum of number of spaces and characters remains constant, i.e 5

for i in range(5):
    print(' '*i,end='')
    for x in range(5-i):
        print(chr(69-i-x),end=' ')
    print()