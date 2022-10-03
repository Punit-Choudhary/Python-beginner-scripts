# This function is used to generate our required pattern.
# It takes an integer n as an input.
def PatternGenerator(n):
    for i in range(0, n-1):
        for j in range(i+1):
            print("*", end=" ")
        for j in range(2*(2*n - 1)-4*(i+1)):
            print(" ", end="")
        for j in range(i+1):
            print("*", end=" ")
        print(' ')
    for i in range(2*n-1):
        print("*", end=" ")
    print(' ')
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            print("*", end=" ")
        for j in range(2*(2*n - 1)-4*(i+1)):
            print(" ", end="")
        for j in range(i+1):
            print("*", end=" ")
        print(' ')


PatternGenerator(4)
# The above line prints the pattern in the image.
