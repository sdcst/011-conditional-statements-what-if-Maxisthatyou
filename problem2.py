#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

x = float(input("Please enter a number> "))
if (x).is_integer():
    print("The number is an integer")
else:
    print("The number is a float")