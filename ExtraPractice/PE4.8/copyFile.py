"""
Write a script named copyFile.py. This script should prompt the user for the names of two
text files. The contents of the first file should be input and written to the second file.

An example of the program input is shown below:

Enter the input file name: copyFrom.txt
Enter the output file name: copyTo.txt

Output: After running the program, a file named copyTo.txt will be
outputted that contains the text from the copyFrom.txt file.
"""

# get the inputs from the user
iFile = input("Enter the input file name: ")
oFile = input("Enter the output file name: ")

f = open(iFile, 'r')  # open the input file
g = open(oFile, 'w')  # create a few file with the oFile name

for x in f.readlines():
    g.write(x)

f.close()
g.close()
