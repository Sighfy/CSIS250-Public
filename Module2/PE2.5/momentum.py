"""
An object’s momentum is its mass multiplied by its velocity.
Write a program that accepts an object’s mass (in kilograms)
and velocity (in meters per second) as inputs, and then outputs its momentum.

Below is an example of the progam input and output:

Mass: 5
Velocity: 2.5

The object's momentum is 12.5
"""

# get user input
mass = float(input("Mass: "))
velocity = float(input("Velocity: "))

# do maths
momentum = mass * velocity

# display results
print("The object's momentum is ", momentum)