# The below function gives the pattern similar to the pyramid pattern 20
# Here there is a triangle with 1 element in the first row,
# 3 elements in second, 5 in third and so on
# all the elements are in increasing order by 1
# I took 3 variables, i.e. spaces, number, row
# first, I print the spaces, then loop over row times and
# print numbers and then print spaces.
# refer picture for clear understanding.
# After every outer iteration, decrease spaces by 1 and increase
# row by 2(as every row has odd elements)
# thus, the pattern can be solved using python

def printPyramid(n):
    spaces = 3*(n-1)
    num = 1
    row = 1
    while spaces >= 0:
        print(" " * spaces, end="")
        for _ in range(row):
            if (num < 10):
                print(" ", end="")
            print(num, end=" ")
            num += 1
        print(" "*spaces, end="")
        print()
        spaces -= 3
        row += 2


printPyramid(5)
