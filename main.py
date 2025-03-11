"""

Dedupe Lists
We need to add a feature to Doc2Doc that merges two lists of items, removes any duplicates, and returns a sorted list of unique items. This is important for consolidating certain documents and metadata.

Assignment
Complete the deduplicate_lists function. It takes two lists as input lst1 and lst2 and an optional reverse boolean, and returns a sorted list of unique elements. If reverse is True, then the returned list should be sorted in descending order. Use sorted() and pass it the reverse parameter.

"""


def deduplicate_lists(lst1, lst2, reverse=False):
    return sorted(list(set(lst1 + lst2)), reverse=reverse)
