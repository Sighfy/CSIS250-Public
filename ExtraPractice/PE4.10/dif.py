"""
Write a script named dif.py. This script should prompt the user for the names of two text
files and compare the contents of the two files to see if they are the same.

If they are, the script should simply output "Yes".
If they are not, the script should output "No", followed by the first lines of each file that differ from each other.

The input loop should read and compare lines from each file, including whitespace and punctuation.
The loop should break as soon as a pair of different lines is found.
----------------------------------------
Comparing files that are the same:

Enter the first file name: one.txt
Enter the second file name: sameAsOne.txt

Yes
----------------------------------------
Comparing files that are different:

Enter the first file name: one.txt
Enter the second file name: differentFromOne.txt

No
abc
xyz
"""

# get the inputs from the user
file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")

# open the two files
f1 = open(file1, 'r')
f2 = open(file2, 'r')

# read the lines onto a list
data1 = f1.readlines()
data2 = f2.readlines()

# compare the two lists
if data1 == data2:
    print("yes")

# compare the two lists and if different, display the difference
for i in range(0, min(len(data1), len(data2))):
    if data1[i] != data2[i]:
        print("no")
        print(data1[i], data2[i])

# close the files
f1.close()
f2.close()
