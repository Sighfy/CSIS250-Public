"""
In Chapter 4, we developed an algorithm for converting from binary to decimal.
You can generalize this algorithm to work for a representation in any base.
Instead of using a power of 2, you will write a program that converts any base
between 2 and 16. Recall that for numbers 10 - 15 we use letters A - F.

In convert.py, define a function named repToDecimal that expects two arguments,
a string, and an integer. The second argument should be the base. For example,
repToDecimal("10", 8) returns 8, whereas repToDecimal("10", 16) returns 16.

- The function should use a lookup table to find the value of any digit. Make sure
    that this table (it is actually a dictionary) is initialized before the function is defined.
- For its keys, use the 10 decimal digits (all strings) and the letters A . . . F (all uppercase).
    The value stored with each key should be the integer that the digit represents.
    (The letter A associates with the integer value 10, and so on.)
- The main loop of the function should convert each digit to uppercase,
    look up its value in the table, and use this value in the computation.

A main function that tests the conversion function with numbers in several bases has been provided.
"""


# Put your code here
def repToDecimal(str, base):
    result = 0
    # initializing a dictionary
    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 'Module7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15}
    for i in str:
        n = dict[i]
        result = base * result + n
    return result


# A main for testing your program
def main():
    """Tests the function."""
    print(repToDecimal('10', 10))
    print(repToDecimal('10', 8))
    print(repToDecimal('10', 2))
    print(repToDecimal('10', 16))


# The entry point for program execution
if __name__ == "__main__":
    main()
