"""
Write a script that inputs a line of encrypted text and a
distance value and outputs plaintext using a Caesar cipher.
The script should work for any printable characters.
An example of the program input and output is shown below:
Enter the coded text: Lipps${svph%
Enter the distance value: 4
Hello world!
"""
# Get the inputs
code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))

plain = ""  # place holder for the plaintext
for ch in code:  # for loop to decrease the character value
    plain += chr(ord(ch) - distance)  # decrease the character value and assign it to plain

print(plain)  # display the output in plain text
