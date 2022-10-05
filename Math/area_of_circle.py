# Import the math library
import math

# Set the variable 'radius' to be the float input by the user
# for the radius of their circle
radius = float(input("What is the radius of your circle?"))

# set the variable 'area' equal to pi time radius squared
area = (math.pi) * (radius**2)

# Convert area to string to avoid printing conflict
area = str(area)

# Print the results
print("The area of your circle is " + area)
