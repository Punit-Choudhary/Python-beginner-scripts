# The Pythagorean Theorem is used to calculate one side
#  of a right angle triangle from two other sides
def PythagoreanTheorem():
    # Getting The Value Of The Shortest Side
    side_a = float(input('Input The Value Of The Shortest Side: '))
    # Getting The Value Of The Second Shortest Side
    side_b = float(input('Input The Value Of The Second Shortest Side: '))

    # Applying the Pythagorean Theorem
    side_c = ((side_a**2) + (side_b**2))**(1/2)

    print('The value of the longest side is:', side_c)


PythagoreanTheorem()
