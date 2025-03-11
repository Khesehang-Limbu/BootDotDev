"""

Intersect
The .intersection() method calculates the intersection of two sets.

The intersection of two sets is a new set that contains all of the elements that are in both original sets

For example:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.intersection(b)
print(c)
# {3, 4}

Assignment
Complete the get_common_formats function using the .intersection() method. It should take in two arguments, formats1 and formats2, each a list of strings representing the file formats supported by two different pieces of software.

It should return a set of strings representing the file formats that are supported by both pieces of software.

"""


def get_common_formats(formats1, formats2):
    return set(formats1).intersection(set(formats2))
