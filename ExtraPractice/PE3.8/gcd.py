"""
The greatest common divisor of two positive integers, A and B,
is the largest number that can be evenly divided into both of
them. Euclid’s algorithm can be used to find the greatest common
divisor (GCD) of two positive integers. You can use this algorithm
in the following manner:

1. Compute the remainder of dividing the larger number by the smaller number.
2. Replace the larger number with the smaller number
    and the smaller number with the remainder.
3. Repeat this process until the smaller number is zero.

The larger number at this point is the GCD of A and B. Write a program
that lets the user enter two integers and then prints each step in the
process of using the Euclidean algorithm to find their GCD.

example:
Enter the smaller number: 5
Enter the larger number: 15

The greatest common divisor is 5
"""
# get the two starting numbers
num1 = float(input("Enter the smaller number: "))
num2 = float(input("Enter the larger number: "))

while num1 != 0:
    # step one from instructions
    remainder = num2 % num1
    # step 2 from the instructions
    num2 = num1
    num1 = remainder
    # step 3 from instructions
    if num1 == 0:
        break
# display the output as the larger number & as an int to ignore the decimal value
print("The greatest common divisor is", int(num2))
