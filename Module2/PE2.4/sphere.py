"""
Write a program that takes the radius of a sphere
(a floating-point number) as input and then outputs the sphere’s:

Diameter (2 × radius)
Circumference (diameter × π)
Surface area (4 × π × radius2)
Volume (4/3 × π × radius3)
For convenience, the program can import the math module.

Below is an example of the program input and output:

Radius = 5

Diameter     : 10.0
Circumference: 31.41592653589793
Surface area : 314.1592653589793
Volume       : 523.5987755982989
"""

# imports
from math import pi

# get the input that's the radius of a sphere
radius = float(input("What is the radius: "))

# do the maths
diameter = radius * 2
circumference = diameter * pi
surfaceArea = 4 * pi * radius ** 2
volume = 4/3 * pi * radius ** 3

# display the results
print("Radius = ", radius)
print("Diameter \t\t: ",diameter,
      "\nCircumference \t: ", circumference,
      "\nSurface area \t: ", surfaceArea,
      "\nVolume \t\t\t: ", volume)

