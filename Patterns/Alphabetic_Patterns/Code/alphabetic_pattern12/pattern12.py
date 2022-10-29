# code for alphabeticpattern12

# outer loop
for row in range(5):
    # inner loop
    for column in range(row+1):
        print(chr(ord("E")-row), end="")
    print()
