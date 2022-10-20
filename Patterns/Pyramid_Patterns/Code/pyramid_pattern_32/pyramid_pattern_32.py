n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i, -1, -1):
        print(chr(65 + k), end='')
    print()
