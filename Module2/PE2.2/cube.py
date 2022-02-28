"""
instructions:
You can calculate the surface area of a cube
if you know the length of an edge.
Write a program that takes the length of an
edge (an integer) as input and prints the
cube’s surface area as output.
An example of the program input and output is shown below:

Enter the cube's edge: 4
The surface area is 96 square units.
"""
# get the variables
cubesEdge = int(input("Enter the cube's edge: "))
cubesSurfaceArea = cubesEdge ** 2 * 6

# print the outcome
print("The surface area is", cubesSurfaceArea, "square units.", end="")