"""
Write a program that accepts the lengths of three sides
of a triangle as inputs. The program output should indicate
whether or not the triangle is a right triangle.

Recall from the Pythagorean theorem that in a right triangle,
the square of one side equals the sum of the squares of the other two sides.

Use The triangle is a right triangle. and The triangle is
not a right triangle. as your final outputs.

An example of the program input and proper output format is shown below:

Enter the first side: 3
Enter the second side: 4
Enter the third side: 5

The triangle is a right triangle.
"""

# get the inputs
s1 = float(input("Enter the first side: "))
s2 = float(input("Enter the second side: "))
s3 = float(input("Enter the third side: "))

# check the pythagorean theorem
if ((s1 ** 2 + s2 ** 2 == s3 ** 2)
        or (s2 ** 2 + s3 ** 2 == s1 ** 2)
        or (s3 ** 2 + s1 ** 2 == s2 ** 2)):
    # print the outputs from the comparison
    print("The triangle is a right triangle")
else:
    print("The triangle is not a right triangle")
