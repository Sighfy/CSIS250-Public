"""
An example of octalToDecimal.py input and output is shown below:

Enter a string of octal digits: 234

The integer value is 156
"""

octalNumber = int(input("Enter a string of octal digits: "))
i = 1
decimal = 0

while octalNumber != 0:
    remainder = octalNumber % 10
    octalNumber //= 10
    decimal += remainder * i
    i *= 8

print("The integer value is", decimal)
