"""
The class Solution is from the Leet Code website.
I turned it into a working function.
"""
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        outp = 0
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if ((i + 1) < len(s)) and dict[s[i + 1]] > dict[s[i]]:
                outp -= dict[s[i]]
            else:
                outp += dict[s[i]]
        return outp
"""


def romanToInt(s):
    outp = 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(s)):
        if ((i + 1) < len(s)) and dict[s[i + 1]] > dict[s[i]]:
            outp -= dict[s[i]]
        else:
            outp += dict[s[i]]
    return outp


def main():
    s = 'DCLXVI'
    print(romanToInt(s))


if __name__ == "__main__":
    main()
