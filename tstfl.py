from logging import raiseExceptions
from math import pi

def area_of_circle(r):
    if r < 0:
        raise ValueError("No negative numbers")
    return pi * (r**2)
    # print (pi * (r**2))

# area_of_circle(-5)