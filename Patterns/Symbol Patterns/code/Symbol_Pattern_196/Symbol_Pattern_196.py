# Created a nested loop in which for first row and first colun 
# printed '*'character and also for mid row and last coumn till mid row
for i in range(5):
    for j in range(3):
        if(i == 0 or i == 2 or j == 0 or (j == 2 and i<3)):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
