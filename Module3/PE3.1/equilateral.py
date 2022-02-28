"""
Write a program that accepts the lengths of
three sides of a triangle as inputs.

The program output should indicate whether
or not the triangle is an equilateral triangle.

Use The triangle is equilateral. and
The triangle is not equilateral. as your final outputs.

An example of the program inputs and output is shown below:

Enter the first side: 2
Enter the second side: 2
Enter the third side: 2

The triangle is equilateral.
"""
# get the three sides
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

# do the comparisons and output
if side1 == side2 and side2 == side3:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")
