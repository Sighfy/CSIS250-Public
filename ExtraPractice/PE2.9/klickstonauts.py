"""
Write a program that takes as input a number of kilometers
and prints the corresponding number of nautical miles.

Use the following approximations:

A kilometer represents 1/10,000 of the distance
between the North Pole and the equator.

There are 90 degrees, containing 60 minutes of arc each,
between the North Pole and the equator.

A nautical mile is 1 minute of an arc.
An example of the program input and output is shown below:

Enter the number of kilometers: 100
The number of nautical miles is 54
"""

# get the inputs from the user
kilometers = float(input("Enter the number of kilometers: "))

# do the conversions
# nautical miles = (kilometers*60*90)/100000
nautMiles = (kilometers*60*90)/10000

# show the output
print("The number of nautical miles is ", nautMiles)
