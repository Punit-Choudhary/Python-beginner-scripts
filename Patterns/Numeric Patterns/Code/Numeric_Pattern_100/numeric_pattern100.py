# This function is used to generate our required pattern.
# It takes an integer n as an input.
# There are two nested for loops in it.
# Outer loop is used to handle the number of rows.
# There are two loops in the second inner loop.
# The first loop is used to handle the space at the start of each row..
# The second loop of the inner loop is used to print the required pattern.
# Then we use outer loop to repeat this.
def PatternGenerator(n):
    for i in range(0, n):
        for j in range(1, 2*(n-i-1)+1):
            print(" ", end="")
        for j in range((2*i)+1, 0, -1):
            print(j, end=" ")
# Inside the loops, we use print() to print empty spaces.
# Later we use print() to print j.
# it starts from twice the row number minus 1 and decrements to 1.
        print('\n')


PatternGenerator(5)
# The above line prints the pattern in the image.
