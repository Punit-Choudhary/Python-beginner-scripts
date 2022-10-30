# Code for Alphabetic Pattern10
def letter_range(start, end):
    # outerloop
    for i in range(start, end):
        # inner loop
        for j in range(65, i + 1):
            print(f"{chr(j)}", end="")
        print()


# calling Function
letter_range(65, 70)
