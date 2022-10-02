# Number of rows to iterate
# Number of columns to work upon
input_rows = 5
input_column = 5
character = chr(ord('A'))
for rows in range(1, input_rows+1):
    for columns in range(input_column):
        print(character, end=" ")
    character = chr(ord('A') + rows)
    print()
