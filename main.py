"""

Zipmap
Let's practice another simple recursive function.

You may not understand recursion just yet, but by following the instructions, you will begin to grasp the fundamentals.

Assignment
Within Doc2Doc we need to map certain properties from one document to properties of another document. Complete the recursive zipmap function.

It takes two lists as input and returns a dictionary where the first list provides the keys and the second list provides the values.

Example usage:

zipped = zipmap(
    ["Avatar: The Last Airbender", "Avatar (in Papyrus font)", "The Last Airbender (Live Action)"],
    [9.9, 6.1, 2.1]
)

print(zipped)
# {
#   'Avatar: The Last Airbender': 9.9,
#   'Avatar (in Papyrus font)': 6.1,
#   'The Last Airbender (Live Action)': 2.1,
# }

Here's the pseudocode:

If either the keys or values list is empty, return an empty dictionary (base case)
Recursively call zipmap on all but the first elements from keys and values
Add the first element of keys to the resulting dictionary, and set its value to the first element in values
Return the updated dictionary

"""


def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}

    resulting_dict = zipmap(keys[1::], values[1::])
    resulting_dict[keys[0]] = values[0]
    return resulting_dict
