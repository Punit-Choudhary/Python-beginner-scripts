from math import pi

outer_radius = int(input('Enter Outer Radius: '))
inner_radius = int(input('Enter Inner Radius: '))
volume = (2/3) * pi * (outer_radius**3 - inner_radius**3)
print("Volume of a Hollow Hemisphere is: {}".format(volume))
