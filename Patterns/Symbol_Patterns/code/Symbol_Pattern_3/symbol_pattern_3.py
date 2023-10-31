# Set the number of rows for the pattern
rows = 5

# Loop through the rows
for i in range(rows):
    # Print leading spaces (in this case, asterisks "*") before the actual pattern
    for j in range(rows - i):
        print(
            "* ", end=""
        )  # Print an asterisk and a space, end with a space to keep everything on the same line

    # Move to the next line to start a new row
    print("\n")
