# Modify the code below
"""
File: newton.py
Project 6.2
Compute the square root of a number (uses recursive function).
1. The input is a number, or enter/return to halt the
   input process.
2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""

import math

# Initialize the tolerance
TOLERANCE = 0.000001


# Implementation of newton method
def newton(x, estimate=1):
    """
   Returns the square root of x."
   """
    # Compute the difference and test#
    # for the base case
    difference = abs(x - estimate ** 2)
    # check whether difference is less
    # then equal to TOLERANCE or not
    if difference <= TOLERANCE:
        return estimate
    else:
        # Recurse after improving the estimate
        return newton(x, (estimate + x / estimate) / 2)


# Implementation of main method
def main():
    ""
    "Allows the user to obtain square roots."
    ""
    # Iterate the loop
    while True:
        # Receive the input number from the user
        x = input("Enter a positive number or enter/return to quit: ")
        # check x is empty space
        # then break the condition
        if x == "":
            break
        # convert x into float value
        x = float(x)
        # Output the result
        # Display statement for program's estimate
        print("The program's estimate is", newton(x, 1))
        # Display statement for python's estimate
        print("Python's estimate is ", math.sqrt(x))


if __name__ == "__main__":
    # call main() method
    main()
