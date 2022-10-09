#Import the math library
import math

#Set the variable 'radius' to be the float input by the user
#for the radius of their cone
radius = float(input("What is the radius of your cone?"))

#Set the variable 'height' to be the float input by the user
#for the radius of their cone
height = float(input("What is the height of your cone?"))

#set the variable 'volume' equal to pi time radius squared multiplied by height
volume =((math.pi) *(radius ** 2)*(height))/3

#Convert volume to string to avoid printing conflict
volume = str(volume)

#Print the results
print("The volume of your cone is " + volume)