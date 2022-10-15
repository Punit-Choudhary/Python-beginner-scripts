from math import pi

oradius = int(input('Enter Outer Radius: '))
iradius = int(input('Enter Inner Radius: '))
volume = (2/3) * pi * (oradius**3-iradius**3)
print("Volume of a Hollow Hemisphere is: {}".format(volume))
