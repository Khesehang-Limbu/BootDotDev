"""

Closure Practice
Remember, a closure is a function that retains the state of its environment. That makes it useful for tracking data as it changes over time, but it can come at the cost of understandability.

When not to use the nonlocal keyword: when the variable is mutable (such as a list, dictionary or set), and you are modifying its contents rather than reassigning the variable. You only need the nonlocal keyword if you are reassigning a variable instead of modifying its contents (which you must do to change immutable values such as strings and integers).

Let's try a closure without the nonlocal keyword.

Assignment
Complete the new_collection function.

It accepts a list of strings, initial_docs.

It should return a function that closes over a copy of initial_docs. This function should accept a string, append that string to the closed-over list, and return the new list.

Do not modify the original initial_docs list!

Example Usage
new_collection = new_collection(["doc1", "doc2", "doc3"])
print(new_collection("doc4"))
# ['doc1', 'doc2', 'doc3', 'doc4']
print(new_collection("doc5"))
# ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']

"""

import functools


def new_collection(initial_docs):
    new_list = initial_docs.copy()

    def append_item_to_list(item):
        new_list.append(item)
        return new_list
    return append_item_to_list


