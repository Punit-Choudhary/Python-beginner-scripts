def pattern(rows_no):
    for i in range(1, rows_no + 1):
        for k in range(1, i):
            print(" ", end = "")
        for j in range(i, rows_no + 1):
            print(j, end = " ")
        print()
     
    for i in range(rows_no - 1, 0, -1):
        for k in range(1, i):
            print(" ", end = "")
        for j in range(i, rows_no + 1):
            print(j, end = " ")
        print()
    
rows_no = 7
 
pattern(rows_no)
 
