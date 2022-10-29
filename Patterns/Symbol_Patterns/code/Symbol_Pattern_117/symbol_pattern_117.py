for row in range(1, 8):
    for col in range(1, 5):
        if (col == 4) or (row + col == 5) or (row - col == 3):
            print("*", end="")
        else:
            print(end=" ")
    print()
