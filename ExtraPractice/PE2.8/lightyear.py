"""
Light travels at 3 × 10^8 meters per second.
A light-year is the distance a light beam travels in one year.

Write a program that calculates and displays the value of a light-year.

Useful facts:

Seconds in a year = 365×24×60^2
Rate = 3×108 meters per second
Below is an example of the correct output format:

Light travels X meters in a year.
"""

# declare variables and values
secondsInAYear = 365 * 24 * 60 ** 2
rate = 3 * 10 ** 8 # meters per second
lightYear = secondsInAYear * rate
# distance is rate * time
# the output
print("light travels", lightYear, "meters in a year.")