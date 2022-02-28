'''
Write and test a program that computes the area of a circle.

Request a number representing a radius as input from the user.
Use the formula 3.14 × radius2 to compute the area.
Output this result with a suitable label.
'''

radius = float(input("Enter the radius: "))
area = 3.14 * (radius*radius)
print("The area is ", area, "square units")