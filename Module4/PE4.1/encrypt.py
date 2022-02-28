"""
Write a script that inputs a line of plaintext and a distance value and outputs an encrypted text using a Caesar cipher.
The script should work for any printable characters.
An example of the program input and output is shown below:
Enter a message: Hello world!
Enter the distance value: 4
Lipps${svph%
"""
# get the inputs
plainText = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

code = ""  # declare the placeholder for code
for ch in plainText:  # create the for loop to increase the character value
    code += chr(ord(ch) + distance)  # increase the character value and assign it to code

print(code)  # print the output code
