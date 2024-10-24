def print_pattern():
    rows = 5  # Number of rows in the pattern
    for i in range(rows, 0, -1):
        # Print leading spaces to align the stars
        print(" " * (rows - i), end="")
        # Print stars for the current row
        print("* " * i)


print_pattern()
