"""
Modify the guessing-game program so that the user
thinks of a number that the computer must guess.

The computer must make no more than the minimum
number of guesses, and it must prevent the user
from cheating by entering misleading hints.
Use I'm out of guesses, and you cheated and Hooray,
I've got it in X tries as your final output.

(Hint: Use the math.log function to compute the minimum number
of guesses needed after the lower and upper bounds are entered.)
"""

# Modify the code below:
import math

# Get the inputs
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

# compute the max amount of guesses possible
max_guesses = round(math.log(larger - smaller + 1, 2))

count = 0
while True:
    count += 1
    myNumber = (smaller + larger) // 2
    print(smaller, larger)
    print("Your number is", myNumber)
    choice = input('Enter =,<, or >: ')
    if choice == '=':
        print("Hooray, I've got it in", count, "tries.")
        break
    elif smaller == larger:
        print("I'm out of guesses, and you cheated")
        break
    elif choice == '<':
        larger = myNumber - 1
    else:
        smaller = myNumber + 1
