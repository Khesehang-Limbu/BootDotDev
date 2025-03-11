"""

Map
Filter
The built-in filter function takes a function and an iterable (in this case a list) and returns an iterator that only contains elements from the original iterable where the result of the function on that item returned True.

filter function

In Python:

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]

Assignment
Complete the remove_invalid_lines function. It accepts a document as input. It should:

Use the built-in filter function and a lambda to return a copy of the input document
Remove any lines that start with a - character.
Keep all other lines and preserve trailing newlines.
For example, this:

* Star Wars episode 1 is underrated
- Star Wars episode 9 is fine
* Star Wars episode 3 is the best


Should become:

* Star Wars episode 1 is underrated
* Star Wars episode 3 is the best

"""


def remove_invalid_lines(document):
    print(document.split("\n"))
    return '\n'.join(filter(is_invalid_line, document.split("\n")))


def is_invalid_line(line):
    if line == "":
        return True
    if line[0] != "-":
        return True
    return False
