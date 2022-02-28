"""
An example of shiftRight.py input and output is shown below:

Enter a string of bits: Hello world!

!Hello world
"""

# get the input
bitString = input("Enter a string of bits: ")

# move the last character to the front of the text
finalString = bitString[-1:] + bitString[0:len(bitString) - 1]
# another way instead of bitString[-1:] is bitString[len(bitString)-1]

# print the output
print(finalString)
