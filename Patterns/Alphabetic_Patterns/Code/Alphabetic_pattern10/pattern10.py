#Code for Alphabetic Pattern10
def letter_range(start, end):
  	# outer loop
    for i in range(start, end):
        # inner loop
        for j in range(65, i + 1):
            print(f"{chr(j)}", end="")
        print()

# calling Function
letter_range(65, 70)