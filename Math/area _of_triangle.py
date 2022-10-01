# Three sides of triangle
side_a = float(input('Enter first side: '))
side_b = float(input('Enter second side: '))
side_c = float(input('Enter third side: '))

# calculate the semi-perimeter
semi_perimeter = (side_a + side_b + side_c) / 2

area = (semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b)
        * (semi_perimeter - side_c)) ** 0.5
print('The area of the triangle is:', area)
