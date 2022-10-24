for row in range(1, 6):
    for col in range(1, 10):
        if (row == 5) or (row + col == 6) or (col - row == 4):
            print("*", end="")
        else:
            print(end=" ")
    print()
