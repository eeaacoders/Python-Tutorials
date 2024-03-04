



# Importing in Python

import math

num = int(input("Enter the number: "))
square_root = math.sqrt(num)

print("The square root is: ",square_root)

# From keyword:
# from  we use to pick the partuiculare function from the module


from math import sqrt

res = sqrt(9)
print(res)

# as keyword: we can assign the function the small trigging name

from math import pi as p

radius = 6
area = p * radius * radius

print("The area is: ",area)

# The dir function it will show that the module contains what

show = (dir(math))
print(show)


# I can check the details of the functions

print(math.sqrt, type(math.sqrt))