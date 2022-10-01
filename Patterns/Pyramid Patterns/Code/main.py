# This function is used to generate our required pattern.
# It takes an integer n as an input.
# There are two nested for loops in it.
# Outer loop is used to handle the number of rows.
# Inner nested loop is used to handle the number of columns.

# Each row of our traingle is comprised of spaces and stars.
# Observing carefully, the first row is made up of n-1 spaces and 1 star.
# And in each subsequent row, spaces derease and stars increase.
# In any row, the number of pyramid and stars remain constant, equal to n

# We make a variable k to hold the number of spaces we need
# afterspaces are printed, we decrease value of k, and print stars
# In this way, after every iteration of outer loop, spaces decrease


def PatternGenerator(n):
    k = n-1  # Stores number of spaces
    for i in range(1, n+1):
        # This Loop Prints spaces
        for j in range(0, k):
            print(' ', end=" ")
        k = k-1
        # This Loop prints stars
        for j in range(0, i):
            print('*  ', end=" ")

        print('\n')


PatternGenerator(8)
