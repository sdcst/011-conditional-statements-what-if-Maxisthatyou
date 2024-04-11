#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
import math
x = float(input("Please enter one side> "))
y = float(input("Please enter a second side> "))
z = float(input("Please enter a third side> "))

hyp = max(x, y, z)

if (hyp == x):
    c = round(x)
    b = round(y)
    a = round(z)
if (hyp == y):
    c = round(y)
    b = round(x)
    a = round(z)
if (hyp == z):
    c = round(z)
    b = round(x)
    a = round(y)

if ( a ** 2 + b ** 2 ) > ( c ** 2 ):
    print("This is an acute triangle")
elif ( a ** 2 + b ** 2 ) < ( c ** 2 ):
    print("This is an obtuse triangle")
else:
    print("This is a right triangle")