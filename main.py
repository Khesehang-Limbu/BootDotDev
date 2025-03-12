"""

Nested Sum
Recursion is hard for all new developers. If you're struggling, that's okay! Take your time. That's why we're doing a few extra practice problems.

Assignment
In Doc2Doc, users can process files or entire directories. We need to know the total size of those files and directories (measured in bytes).

Due to the nested nature of directories, we represent a root directory as a list of lists. Each list represents a directory, and each number represents the size of a file in that directory. For example, here's a directory that contains 2 files at the root level, then a nested directory with its own two files:

root = [
    1,
    2,
    [3, 4]
]
print(sum_nested_list(root))
# 10

Here's a more complex example:

root
├── scripts.txt (5 bytes)
├── characters (dir)
│   ├── zuko.txt (6 bytes)
│   └── aang.txt (7 bytes)
└── seasons (dir)
    ├── season1 (dir)
    │   ├── the_avatar_returns.docx (8 bytes)
    │   └── the_southern_air_temple.docx (9 bytes)
    └── season2_notes.txt (10 bytes)


Which would be represented as:

root = [
    5,
    [6, 7],
    [[8, 9], 10]
]
print(sum_nested_list(root))
# 45

Complete the sum_nested_list function. It takes a nested list of integers as input and should return the total size of all files in the list. It's a recursive function.

Here's some pseudocode to help you get started:

Create an integer variable to keep track of the total size.
For each item in the list (use a loop here):
If the item is an integer, add it to the total size.
If the item is a list, use a recursive call to sum_nested_list to get the size of that list. Add that size to the total size.
Return the total size when you're done iterating.

"""


def sum_nested_list(lst):
    total_size = 0

    for item in lst:
        if isinstance(item, int):
            total_size += item
        elif isinstance(item, list):
            total_size += sum_nested_list(item)
    return total_size

