"""

Reference vs. Value
When you pass a value into a function as an argument, one of two things can happen:

It's passed by reference: The function has access to the original value and can change it
It's passed by value: The function only has access to a copy. Changes to the copy within the function don't affect the original
There is a bit more nuance, but this explanation mostly works.

These types are passed by reference:

Lists
Dictionaries
Sets
These types are passed by value:

Integers
Floats
Strings
Booleans
Tuples
Most collection types are passed by reference (except for tuples) and most primitive types are passed by value.

Example of Pass by Reference (Mutable)
def modify_list(inner_lst):
    inner_lst.append(4)
    # the original "outer_lst" is updated
    # because inner_lst is a reference to the original

outer_lst = [1, 2, 3]
modify_list(outer_lst)
# outer_lst = [1, 2, 3, 4]

Example of Pass by Value (Immutable)
def attempt_to_modify(inner_num):
    inner_num += 1
    # the original "outer_num" is not updated
    # because inner_num is a copy of the original

outer_num = 1
attempt_to_modify(outer_num)
# outer_num = 1

Assignment
We have a way for Doc2Doc users to set their supported formats in their settings. In memory, we store those settings as a simple dictionary:

settings = {
    "docx": True,
    "pdf": True,
    "txt": False
}

Unfortunately, there is a bug in our code! When a new format is added or removed, it not only updates the new dictionary, but it changes the defaults themselves! That's not good. We want to create a new dictionary with the updates, not change the original.

Fix the bug by making add_format and remove_format pure functions that don't mutate their inputs.


"""


def add_format(default_formats, new_format):
    mutated_formats = default_formats.copy()
    mutated_formats[new_format] = True
    return mutated_formats


def remove_format(default_formats, old_format):
    mutated_formats = default_formats.copy()
    mutated_formats[old_format] = False
    return mutated_formats
