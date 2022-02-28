"""
File: decrypt.py
Project 4.3

Decypts a file of encryptedtext text. and prints
the result.  The other input is the distance value.
the decrypted code is written to a new file
"""

# Get the inputs
file = input("Enter the input file name: ")
newFile = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

f = open(file, 'r')  # open the input file
g = open(newFile, 'w')  # create a new file with the newFile name

while True:
    code = f.readline()  # read the coded text

    plain = ""  # place holder for the plaintext
    for ch in code:  # for loop to decrease the character value
        plain += chr(ord(ch) - distance)  # decrease the character value and assign it to plain

    print(plain)  # display the output in plain text
    g.write(plain)  # write to the new file

    if code == "":
        f.close()  # close the input file
        g.close()  # close the output file
        break
