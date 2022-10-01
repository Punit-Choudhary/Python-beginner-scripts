#Created a nested loop of 7*7
#printed '*' character at row 7 coloumn 7 and diagonal
#else printed space and later added new line after each row iteration
for i in range(8):
    for j in range(8):
        if(i==7 or j==7 or i==j):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()