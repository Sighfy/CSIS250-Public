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

# Initialize the tolerance
TOLERANCE = 0.000001


# this is the Newton's function
def newton(x, estimate):
    # new value of estimate being calculated
    estimate = (estimate + x / estimate) / 2
    # here we are considering the absolute value i.e just the magnitude
    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        # we are returning the value of estimate if the difference is less than the tolerance value set
        return estimate
    else:
        # here is the recursive function being executed
        # we are calling the newton function passing the user input and the new estimate value,
        # we are passing the estimate value as the second argument to the function
        return newton(x, estimate)


def main():
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        # Output the result
        estimate = 1.0
        print("The program's estimate is", newton(x, estimate))
        print("Python's estimate is ", math.sqrt(x))


if __name__ == "__main__":
    main()
