for row in range(1, 8):
    for col in range(1, 5):
        if (col == 1) or (row - col == 0) or (row + col == 8):
            print("*", end="")
        else:
            print(end=" ")
    print()
