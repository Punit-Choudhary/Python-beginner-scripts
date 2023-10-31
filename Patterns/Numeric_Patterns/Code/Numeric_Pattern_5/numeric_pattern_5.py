# Defining a function
def Numeric_Pattern_1(num):
    counter = 1  # Initialize a counter to start with 1

    # Making a loop
    for x in range(num):
        # Making a nested loop printing the numbers
        for y in range(num):
            print(counter, end=" ")
            counter += 1  # Increment the counter

        # Adding a new line after each row
        print("")


# Calling the function
Numeric_Pattern_1(5)
