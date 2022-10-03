# Defining the function to calculate the circumference of a circle
def Circumference():
    PI = 3.14159
    radius = float(input('Enter Radius Of Circle: '))

    # The formula to calculate circumference
    circumference = 2 * PI * radius

    print('The Circumference Of The Circle Is:', circumference)


Circumference()
