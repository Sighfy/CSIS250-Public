"""
Write a program that allows the user to navigate the lines of text in a file.
The program should prompt the user for a filename and input the lines of text
into a list. The program then enters a loop in which it prints the number of
lines in the file and prompts the user for a line number. Actual line numbers
range from 1 to the number of lines in the file. If the input is 0, the program
quits. Otherwise, the program prints the line associated with that number.

Example:
Enter the input file name: example.txt

The file has 3 lines.
Enter a line number [0 to quit]: 2
2 :  Line 2.
The file has 3 lines.
Enter a line number [0 to quit]: 4
ERROR: line number must be less than 3.
The file has 3 lines.
Enter a line number [0 to quit]: 0
"""

iFile = input("Enter the input file name: ")  # get the input
f = open(iFile, 'r')  # open the file
contentList = f.readlines()  # read the contents of the file into a list
length = len(contentList)  # find the length of the list
while True:
    print("The file has", length, "lines.")  # display how many lines there are (the length of the list)
    number = int(input("Enter a line number [0 to quit]: "))  # get the user input for the problem
    if number == 0:  # check for a 0 to quit
        break
    if number > length:  # check to make sure the number is in bounds
        print("ERROR: line number must be less than ", length, ".")  # disaply the error message for out of bound
    else:
        print(number, ":", contentList[number - 1])  # print the requested line, -1 because lists start at 0 not 1
f.close()  # close the file
