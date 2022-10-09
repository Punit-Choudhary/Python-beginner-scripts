#Import the math library
import math

#Set the variable 'length' to be the float input by the user
#for the length of their cuboid
length = float(input("What is the length of your cuboid?"))

#Set the variable 'height' to be the float input by the user
#for the height of their cuboid
height = float(input("What is the height of your cuboid?"))

#Set the variable 'breadth' to be the float input by the user
#for the breadth of their cuboid
breadth = float(input("What is the breadth of your cuboid?"))

#set the variable 'volume' equal to length multiplied by breadth multiplied by height
volume =(length)*(breadth)*(height)

#Convert volume to string to avoid printing conflict
volume = str(volume)

#Print the results
print("The volume of your cuboid is " + volume)