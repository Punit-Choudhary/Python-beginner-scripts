# In a nested loop i is iterated for certain constraints on row
# and j is iterated for certain conditions i=on column
# and accordingly '*' character or space is added
x = int(input('Enter Number :'))
# Enter dimensions of square box for which we want to draw pattern
if (x%2 == 0):
    x += 1
# Make sure that inputted number is odd or else make it odd
for i in range(x):  # iterations for rows
    for j in range(x):  # iterations for column
        if (i == 0 or j == 0):
            print("*", end=' ')
        elif (i == (x-1)//2):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()  # new line entered for creating pattern
