for row in range(1, 6):
    for col in range(1, 10):
        if (row == 1) or (row + col == 10) or (col - row == 0):
            print("*", end="")
        else:
            print(end=" ")
    print()
