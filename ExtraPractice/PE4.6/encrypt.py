"""
Use the strategy of the decimal to binary conversion implemented in Project 4,
and the bit shift left operation defined in Project 5 to code a new encryption algorithm.

The algorithm should
    1. Add 1 to each character’s numeric ASCII value.
    2. Convert it to a bit string.
    3. Shift the bits of this string one place to the left.
A single-space character in the encrypted string separates the resulting bit strings.
An example of the program input and output is shown below:
Enter a message: Hello world!

0010011 1001101 1011011 1011011 1100001 000011 1110001 1100001 1100111 1011011 1001011 000101
"""
plainText = input("Enter a message: ")

code = ""
for ch in plainText:
    # Add 1 to ASCII value
    ordValue = ord(ch) + 1
    # Convert to binary
    bstring = ""
    while ordValue > 0:
        remainder = ordValue % 2
        ordValue = ordValue // 2
        bstring = str(remainder) + bstring
    # Shift one bit to left
    if len(bstring) > 1:
        bstring = bstring[1:] + bstring[0]
    # Add encrypted character to code string
    code += bstring + " "
print(code)
