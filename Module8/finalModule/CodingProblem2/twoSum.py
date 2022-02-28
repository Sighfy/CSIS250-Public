"""
The first second interview problem from the class.

Given an array of integers, return indices of two numbers from
this array such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

The class was given, but turned into a function below for testing in the PyCharm IDE.

This problem can be found on the leet code website.
"""

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create an empty dictionary
        dictionary = {}
        answer = []
        # for each number in list of numbers
        for i in range(len(nums)):
            # result = substraction number from target number
            secondNumber = target - nums[i]
            # look for result in the dictionary
            if (secondNumber in dictionary.keys()):
                # if found, return index of number and index of dictionary lookup result
                secondIndex = nums.index(secondNumber)
                if (i != secondIndex):
                    # if not found, add number to dictionary as key with value being the index
                    return sorted([i, secondIndex])

            dictionary.update({nums[i]: i})
"""


def twoSum(nums, target):
    # create an empty dictionary
    dictionary = {}
    answer = []
    # for each number in list of numbers
    for i in range(len(nums)):
        # result = subtraction number from target number
        secondNumber = target - nums[i]
        # look for result in the dictionary
        if (secondNumber in dictionary.keys()):
            # if found, return index of number and index of dictionary lookup result
            secondIndex = nums.index(secondNumber)
            if (i != secondIndex):
                # if not found, add number to dictionary as key with value being the index
                return sorted([i, secondIndex])

        dictionary.update({nums[i]: i})


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))


if __name__ == "__main__":
    main()
