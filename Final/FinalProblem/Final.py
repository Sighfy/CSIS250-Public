"""
Define a function  print_pyramid(type, height).
The values for the type argument could be either "left", "right", "both".
The height parameters should determine how high of the pyramid in rows.
"""


# function to print the pyramid
def print_pyramid(t, h):
    # check for type left
    if t == "left":
        for i in range(h):
            # needs to be right adjusted
            print(" " * (h - i) + "#" * (i + 1))
    # check for type right
    elif t == "right":
        for i in range(h):
            print("#" * (i + 1))
    # check for type both
    elif t == "both":
        for i in range(h):
            # print the left one then the right one next to it
            print(" " * (h - i - 1) + "#" * (2 * i))


def main():
    # get the type option
    t = input('Please enter "left", "right", or "both": ')
    # get the height
    h = int(input("Please enter the height of the pyramid: "))
    # pass the type and height to the function to print
    print_pyramid(t, h)


if __name__ == "__main__":
    main()
