"""
File: filesys.py
Project 6.6

Provides a menu-driven tool for navigating a file system
and gathering information on files.

Adds a command to view a file's contents.
"""

import os, os.path

QUIT = '8'

COMMANDS = ('1', '2', '3', '4', '5', '6', 'Module7', '8')  # added the missing 7th number

MENU = """  
1   List the current directory
2   Move up
3   Move down
4   Number of files in the directory
5   Size of the directory in bytes
6   Search for a file name
Module7   View the contents of a file
8   Quit the program
"""  # added the missing 7th option


def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            break


def acceptCommand():
    """Inputs and returns a legitimate command number."""
    while True:
        command = input("Enter a number: ")
        if not command in COMMANDS:
            print("Error: command not recognized")
        else:
            return command


def runCommand(command):
    """Selects and runs a command."""
    if command == '1':
        listCurrentDir(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown(os.getcwd())
    elif command == '4':
        print("The total number of files is",
              countFiles(os.getcwd()))
    elif command == '5':
        print("The total number of bytes is",
              countBytes(os.getcwd()))
    elif command == '6':
        target = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found")
        else:
            for f in fileList:
                print(f)
    # add your condition here
    elif command == 'Module7':  # added the 7th option for the viewFile method
        viewFile(os.getcwd())


# view files method for the assignment
def viewFile(dirName):
    # write your code here
    lyst = list(filter(os.path.isfile, os.listdir(dirName)))
    if len(lyst) == 0:  # check for empty directory
        print("There are no files in this directory")
    else:
        while True:
            print("Files in " + dirName + ":")  # print the directory you're in
            for element in lyst:  # print the files in the directory
                print(element)
            fileName = input("Enter a file name from these names: ")
            if not fileName in lyst:  # check for invalid file name
                print("Sorry, there is an error in your file name.")
            else:  # with valid file name
                f = open(fileName, 'r')  # open the files
                print(f.read())  # print the contents of the file
                f.close()  # close the file
                break  # only break once a valid input has been done


def listCurrentDir(dirName):
    """Prints a list of the cwd's contents."""
    lyst = os.listdir(dirName)
    for element in lyst: print(element)


def moveUp():
    """Moves up to the parent directory."""
    os.chdir("..")


def moveDown(currentDir):
    """Moves down to the named subdirectory if it exists."""
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and \
            os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("ERROR: no such name")


def countFiles(path):
    """Returns the number of files in the cwd and
    all its subdirectories."""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    return count


def countBytes(path):
    """Returns the number of bytes in the cwd and
    all its subdirectories."""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count


def findFiles(target, path):
    """Returns a list of the file names that contain
    the target string in the cwd and all its subdirectories."""
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(findFiles(target, os.getcwd()))
            os.chdir("..")
    return files


if __name__ == "__main__":
    main()
