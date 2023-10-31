# Set the number of rows for the pattern
n = 5

# Loop through rows from 1 to 'n'.
for i in range(1, n + 1):

    # Loop to print spaces before the numbers in each row.
    for k in range(1, n - i + 1):
        print(" ", end=" ")

    # Loop to print numbers in ascending order in each row.
    for j in range(1, i + 1):
        print(j, end=" ")

    # Move to the next line to start a new row.
    print()
