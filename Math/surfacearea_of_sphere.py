# Import the math library
import math

# Set the variable 'radius' to be the float input by the user
# for the radius of their sphere
radius = float(input("What is the radius of your sphere?"))

# set the variable 'surfacearea' equal to pi time radius squared mulplied by 4
surfacearea = 4*(math.pi) * (radius**2)

# Convert surfacearea to string to avoid printing conflict
surfacearea = str(surfacearea)

# Print the results
print("The surface area of your sphere is " + surfacearea)