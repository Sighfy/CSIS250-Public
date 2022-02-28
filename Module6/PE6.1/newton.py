# Modify the code below
"""
File: newton.py
Project 6.1

Compute the square root of a number (uses function with loop).

1. The input is a number, or enter/return to halt the
   input process.

2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""

import math


# define the newton function for finding the outputs
def newton(x):
    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0

    # Perform the successive approximations
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
    return estimate


# define the main function
def main():
    while True:
        try:
            # Receive the input number from the user
            x = float(input("Enter a positive number/return to quit: "))

            # Output the result
            print("The program's estimate is", newton(x))
            print("Python's estimate is", math.sqrt(x))
        except:
            return


if __name__ == "__main__":
    main()
