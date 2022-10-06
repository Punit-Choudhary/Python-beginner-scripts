# Defining a function
def Numberic_Pattern_1(num):
    # Making a loop
    for x in range(1, num):
        # Separating the numbers by each row
        print('')
        # Making a nested loop printing the numbers
        for y in range(num):
            print(x, end='')
    # Adding an extra line at the end. Can also use \n
    print('')


# Calling the function
Numberic_Pattern_1(6)
