# This function is used to generate our required pattern.
# It takes an integer n as an input.
# There are two nested for loops in it.
# Outer loop is used to handle the number of rows.
# Inner nested loop is used to handle the number of columns.
# Think of it in this way, using the inner loop, we print 1 2 3 4 5.
# Then we use outer loop to repeat this.
def PatternGenerator(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(j, end=" ")
# Inside the loops, we use print() to print the value j.
# j starts from 1 and as the loop goes on,
# it increments its value and prints other numbers
        print('\n')


PatternGenerator(5)
