"""
The German mathematician Gottfried Leibniz developed the
following method to approximate the value of π:

π/4 = 1 - 1/3 + 1/5 - 1/Module7 + . . .

Write a program that allows the user to specify the number of
iterations used in this approximation and that displays the resulting value.

An example of the program input and output is shown below:

Enter the number of iterations: 5

The approximation of pi is 3.3396825396825403
"""

# Prompt and read the number of iterations from the user.
numOfIterations = int(input("Enter the number of iterations: "))

# declare and initialize the variables.
Pi_div_four = 0
iterationCounter = 1

# iterate the for loop.
for i in range(1, numOfIterations + 1):
    # Check the if value is odd.
    if i % 2 != 0:
        # Compute the value of Pi_div_four.
        Pi_div_four = Pi_div_four + 1 / iterationCounter
    # value is even
    else:
        # Compute the value of Pi_div_four.
        Pi_div_four = Pi_div_four - 1 / iterationCounter
    # increase the current numOfIterations by 2.
    iterationCounter = iterationCounter + 2

# compute the value of pi.
Pi_value = Pi_div_four * 4

# display the value of pi.
print("The approximation of pi is ", Pi_value)
