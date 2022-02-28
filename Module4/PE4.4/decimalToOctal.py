"""
An example of decimalToOctal.py input and output is shown below:

Enter a decimal integer: 27

Quotient Remainder Octal
    3       3           3
    0       3          33
The octal representation is 33
"""

decimalNumber = int(input("Enter a decimal integer: "))
print("Quotient remainder Octal")

i = 1
octalNumber = 0
num = ""

while decimalNumber != 0:
    remainder = decimalNumber % 8
    decimalNumber //= 8  # floor division
    octalNumber += remainder * i
    i *= 10
    num = str(remainder) + num

    print("%5d%8d%12s" % (decimalNumber, remainder, num))

print("The octal representation is", octalNumber)
