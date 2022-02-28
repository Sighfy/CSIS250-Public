"""
An example of shiftLeft.py input and output is shown below:

Enter a string of bits: Hello world!

ello world!H
"""

# get the input
bitString = input("Enter a string of bits: ")

# move the first character to the back
finalString = bitString[1:] + bitString[0]

# print the result
print(finalString)
