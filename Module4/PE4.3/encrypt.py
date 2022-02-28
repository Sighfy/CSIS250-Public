"""
File: encrypt.py
Project 4.3

Encypts a text file.  The inputs are the names of
the input file and the output file and the distance value.
The encryptedtext code is witten to a new file.
"""

# Get the inputs
file = input("Enter the input file name: ")
newFile = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

f = open(file, 'r')  # open the input file
g = open(newFile, 'w')  # create a new file with the newFile name

while True:
    plainText = f.readline()  # read the plaintext

    coded = ""  # place holder for the coded text
    for ch in plainText:  # for loop to increase the character value
        coded += chr(ord(ch) + distance)  # increase the character value and assign it to plain

    print(coded)  # display the output in coded text
    g.write(coded)  # write to the new file

    if plainText == "":
        f.close()  # close the input file
        g.close()  # close the output file
        break
