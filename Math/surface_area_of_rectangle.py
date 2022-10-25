# Taking the values of Length, Breadth and Height from user
length = float(input('Enter the length of the Cuboid: '))
breadth = float(input('Enter the breadth of the Cuboid: '))
height = float(input('Enter the height of the Cuboid: '))

# Calculating the Total Surface Area of the Cuboid
tsa = (2 * ((length * breadth) + (breadth * height) + (length * height)))

# Calculating the Lateral Surface Area of the Cuboid
lsa = (2 * (length + breadth) * height)

# Printing the Surface Areas
print("The Total Surface Area of the cuboid is: ", tsa)
print("The Lateral Surface Area of the cuboid is: ", lsa)
