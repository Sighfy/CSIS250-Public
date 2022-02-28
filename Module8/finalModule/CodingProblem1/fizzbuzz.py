"""
The first coding problem from the class.

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and
for the multiples of five output “Buzz”. For numbers which are multiples of
both three and five output “FizzBuzz”.

The class was given, but turned into a function below for testing in the PyCharm IDE.

This problem can be found on the leet code website.
"""

"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for num in range(1, n + 1):

            if num % 3 == 0 and num % 5 == 0:
                # Divides by both 3 and 5, add FizzBuzz to list
                ans.append("FizzBuzz")
            elif num % 3 == 0:
                # Divides by 3, add Fizz to list
                ans.append("Fizz")
            elif num % 5 == 0:
                # Divides by 5, add Buzz to list
                ans.append("Buzz")
            else:
                # Not divisible by 3 or 5, add the number to list
                ans.append(str(num))
        # returns the answer as a list
        return ans
"""


def fizzBuzz(n):
    ans = []

    for num in range(1, n + 1):

        if num % 3 == 0 and num % 5 == 0:
            # Divides by both 3 and 5, add FizzBuzz to list
            ans.append("FizzBuzz")
        elif num % 3 == 0:
            # Divides by 3, add Fizz to list
            ans.append("Fizz")
        elif num % 5 == 0:
            # Divides by 5, add Buzz to list
            ans.append("Buzz")
        else:
            # Not divisible by 3 or 5, add the number to list
            ans.append(str(num))
    # returns the answer as a list
    return ans


def main():
    n = 15
    print(fizzBuzz(n))


if __name__ == "__main__":
    main()
