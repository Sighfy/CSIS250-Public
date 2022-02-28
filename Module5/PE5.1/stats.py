"""
A group of statisticians at a local college has asked you to create a set of functions
that compute the median and mode of a set of numbers. Define these functions, median
and mode, in a module named stats.py. Also include a function named mean, which computes
the average of a set of numbers. Each function should expect a list of numbers as an
argument and return a single number. Each function should return 0 if the list is empty.
Include a main function that tests the three statistical functions using the following
list defined in main:

list = [3, 1, Module7, 1, 4, 10]

example:
List: [3, 1, Module7, 1, 4, 10]
Mode: 1
Median: 3.5
Mean: 4.33333333333333
"""


def mode(lyst):
    frequency = {}
    for number in lyst:
        frequency.setdefault(number, 0)
        frequency[number] += 1
    highestFrequency = max(frequency.values())
    highestFrequencyList = []
    for number, freq in frequency.items():
        if freq == highestFrequency:
            highestFrequencyList.append(number)
    numberList = highestFrequencyList[0]
    return (numberList)


def median(lyst):
    length = len(lyst)
    lyst.sort()

    if length % 2 == 0:
        median1 = lyst[length // 2]
        median2 = lyst[length // 2 - 1]
        median = (median1 + median2) / 2
        return median
    else:
        median = lyst[length // 2]
        return median


def mean(lyst):
    return sum(lyst) / len(lyst)


def main():
    lyst = [3, 1, 7, 1, 4, 10]

    print("list: ", lyst)
    print("Mode: ", mode(lyst))
    print("Median: ", median(lyst))
    print("Mean: ", mean(lyst))


main()
