# Number of rows to iterate
# Number of columns to work upon
input_rows = 5
input_columns = 5

for rows in range(input_rows):
    for columns in range(1, input_columns + 1):
        print(chr(ord("A") + columns - 1), end=" ")
    print()
