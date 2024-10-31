import cmath

def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' must be non-zero for a quadratic equation.")

    discriminant = b**2 - 4 * a * c

    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return root1, root2

try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    roots = solve_quadratic(a, b, c)
    print(f"The roots of the equation are: {roots[0]} and {roots[1]}")
except ValueError as e:
    print(e)
