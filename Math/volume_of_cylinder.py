# Import the math library
import math

# Set the variable 'radius' to be the float input by the user
# for the radius of their cylinder
radius = float(input("What is the radius of your cylinder?"))

# Set the variable 'height' to be the float input by the user
# for the height of their cylinder
height = float(input("What is the height of your cylinder?"))

# set the variable 'volume' equal to pi times
# radius squared multiplied by height
volume = (math.pi) * (radius**2) * (height)

# Convert volume to string to avoid printing conflict
volume = str(volume)

# Print the results
print("The volume of your cylinder is " + volume)
