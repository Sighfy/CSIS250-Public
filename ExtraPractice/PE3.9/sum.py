"""
Edit the program provided so that it receives a series of numbers from the
user and allows the user to press the enter key to indicate that he or she
is finished providing inputs. After the user presses the enter key,
the program should print:

1. The sum of the numbers
2. The average of the numbers

example:
Enter a number or press Enter to quit: 1
Enter a number or press Enter to quit: 2
Enter a number or press Enter to quit: 3
Enter a number or press Enter to quit:

The sum is 6.0
The average is 2.0
"""
# Edit the code below

theSum = 0.0
# changed the input text
data = input("Enter a number or press Enter to quit: ")
# the math for the addition appears to be correct, need to create the average
# -- use a sentinel counter to divide by
# 'i' is the sentinel
i = 0
while data != "":
    # increment the sentinel
    i += 1
    number = float(data)
    theSum += number
    # changed the input text
    data = input("Enter a number or press Enter to quit: ")

# do the division for the average, sum / sentinel = average
avg = theSum / i
print("The sum is", theSum)
# add the output for the avg
print("The average is", avg)
