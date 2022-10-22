def squaresum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


n = int(input("Enter the value: "))
print(squaresum(n))
