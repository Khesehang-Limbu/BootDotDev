"""

Recursive String Reversal
At Doc2Doc we need to be able to reverse strings. Our bad-word detection algorithms need to work on those crazy teenagers who write unpleasantries backward to try to get around our filters!

However, being an ex-Haskell-loving university professor, our team lead has asked us to implement it using recursion instead of a loop.

Assignment
Complete the reverse_string function.

It should take a string as a parameter and return the reversed string by recursively reversing the substrings inside. Your function should recurse once for each character in the string.

"""


def reverse_string(s):
    reversed_string = ""

    if len(s) == 1 or s == "":
        return s

    reversed_string += s[len(s)-1]
    reversed_string += reverse_string(s[:len(s)-1:])

    return reversed_string
