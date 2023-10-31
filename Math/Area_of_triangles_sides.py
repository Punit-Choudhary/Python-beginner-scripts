print("Calculate the area of triangle through sides \n")

# Input values of sides
s1 = float(input("Enter the value of A :"))
s2 = float(input("Enter the value of B :"))
s3 = float(input("Enter the value of C :"))

# Defining the formula of Heron's to calculate the area of triangle.
def Area(a, b, c):
    sp = (a + b + c) / 2
    area = (sp) * (sp - a) * (sp - b) * (sp - c)
    f_area = round((area**0.5), 2)
    print(f"{f_area}" + " square units")


# Printing the area of triangle.
Area(s1, s2, s3)
