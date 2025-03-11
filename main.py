"""

Memoization
At its core, memoization is just caching (storing a copy of) the result of a computation so that we don't have to compute it again in the future.

For example, take this simple function:

def add(x, y):
    return x + y

A call to add(5, 7) will always evaluate to 12. So, if you think about it, once we know that add(5, 7) can be replaced with 12, we can just store the value 12 somewhere in memory so that we don't have to do the addition operation again in the future. Then, if we need to add(5, 7) again, we can just look up the value 12 instead of doing a (potentially expensive) CPU operation.

The slower and more complex the function, the more memoization can help speed things up.

Note: It's pronounced "memOization", not "memORization". This confused me for quite a while in college, I thought my professor just didn't speak goodly...

Assignment
Counting the words in a document can be slow, so we want to memoize it.

Complete the word_count_memo function. It takes two inputs:

A document string.
A memos dictionary. The keys are full document strings, and the values are the word count of the document.
It should return two values:

The word count of the given document
An updated memos dictionary.
Here are the steps to follow:

Create a .copy() of the memos dictionary.
If the document is in the memos dictionary, just return the associated word count and the memos copy. No need to recompute the word count.
Otherwise, use the provided word_count function to count the words in the given document.
Store the word count in the memos copy.
return the word count and the updated memos copy.

"""


def word_count_memo(document, memos):
    memos_copy = memos.copy()
    if document in memos_copy.keys():
        return memos_copy[document], memos_copy

    new_count = word_count(document)
    memos_copy[document] = new_count
    return new_count, memos_copy


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
