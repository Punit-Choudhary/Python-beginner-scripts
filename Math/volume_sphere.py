# Import the math library
import math

# Set the variable 'radius' to be the float input by the user
# for the radius of their cylinder
radius = float(input("What is the radius of your sphere?"))

# set the variable 'volume' equal to pi times
# radius squared multiplied by height
volume = 4* (math.pi) * (radius**3) /3  # 4/3(pi*r^3)

# Convert volume to string to avoid printing conflict
volume = str(volume)

# Print the results
print("The volume of your sphere is " + volume)
