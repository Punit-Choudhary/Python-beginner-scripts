def numeric_pattern_4(num):
    # Loop to keep track of rows
    for i in range(num):
        # Loop for keeping track of column
        for j in range(num, 0, -1):
            print(j, end=" ")
        print()


numeric_pattern_4(6)
