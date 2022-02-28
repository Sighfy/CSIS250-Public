"""
Write a script named numberlines.py. This script creates a program listing from a source program.

This script should:
1. Prompt the user for the names of two files.
    - The input filename could be the name of the script itself,
        but be careful to use a different output filename!
2. The script copies the lines of text from the input file to the output file,
    numbering each line as it goes.
3. The line numbers should be right-justified in 4 columns, so that the
    format of a line in the output file looks like this example:
      1> This is the first line of text.
"""

# get the inputs from the user
iFile = input("Enter the input file name: ")
oFile = input("Enter the output file name: ")

f = open(iFile, 'r')  # open the input file
g = open(oFile, 'w')  # create a few file with the oFile name

i = 0  # the sentinel for the numbered lines
for x in f.readlines():
    i += 1  # add to the sentinel
    g.write("{:>4}> {}".format(i, x))  # format the number right justified by 4 and print the lines

f.close()  # close the input file
g.close()  # close the output file

"""
# here is another way to accomplish the same thing


input_filename = input('Enter input file name: ')
output_filename = input('Enter output file name: ')

with open(input_filename, 'r') as f, open(output_filename, 'w') as w:
    number = 0
    for line in f:
        number += 1
        w.write('{:>4}> {}'.format(number, line))

"""

