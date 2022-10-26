# Import the math library
import math

# Set the variable 'a' to be the float input by the user
# for the length of the semi-major axis of their ellipse
a = float(input("\nWhat is the length of the semi-major axis of your ellipse? : "))

# Set the variable 'b' to be the float input by the user
# for the length of the semi-minor axis of their ellipse
b = float(input("\nWhat is the length of the semi-minor axis of your ellipse? : "))

# set the variable 'area' equal to the product of pi, a, and b
area = (math.pi) * (a) * (b)

# Convert area to string to avoid printing conflict
area = str(area)

# Print the results
print("The area of your ellipse is approximately " + area)
