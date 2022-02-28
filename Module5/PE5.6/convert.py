"""
In convert.py, define a function decimalToRep that returns the representation of an integer in a given base.

* The two arguments should be the integer and the base.
* The function should return a string.
* It should use a lookup table that associates integers with digits.

A main function that tests the conversion function with numbers in several bases has been provided.

An example of main and correct output is shown below:
"""


# Put your code here
def decimalToRep(num, base):
    result = ""
    while (num > 0):
        rem = num % base  # get the remainder
        if rem in range(10):  # if the remainder is in range
            result += str(rem)  # turn the remainder into a string
        else:  # only base 16 will go to this else
            result += chr(65 + (rem % 10))  # character conversion for ASCII values
        num = num // base
    result = result[::-1]
    if (result == ""):  # if it is blank return a 0
        return '0'
    return result


# A main for testing your program
def main():
    """Tests the function."""
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))


# The entry point for program execution
if __name__ == "__main__":
    main()
