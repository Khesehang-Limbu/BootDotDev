"""
Differences
The Fantasy Quest team merged some of the servers together, but the merge didn't go perfectly. The resulting lists have duplicates and missing IDs. We need to clean up the duplicates and find the missing IDs.

Assignment
Complete the find_missing_ids function. It accepts two lists as input, and returns a new list of all the IDs that are in the first list but are not in the second. Make sure to remove any duplicates.
"""

def find_missing_ids(first_ids, second_ids):
    return list(set(first_ids) - set(second_ids))

