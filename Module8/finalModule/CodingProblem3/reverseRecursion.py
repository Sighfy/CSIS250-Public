"""
The third coding problem from the class.

Write a function that reverses a python list using recursion
(Chapter 6-3 in our textbook)
"""


def rev(inlist):
    # return a blank if the list is blank
    if len(inlist) == 0:
        return []
    # check to see if there is only one element in the list
    # then add the numbers back to the list in reverse order
    elif len(inlist) == 1:
        return inlist
    # subtract each number from the list in reverse order
    # then add the numbers back to the list in reverse order
    return [inlist[len(inlist) - 1]] + rev(inlist[:len(inlist) - 1])


def main():
    # create the input list
    inlist = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # print the input list
    print(rev(inlist))


if __name__ == "__main__":
    main()
