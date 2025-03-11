"""

Restore
Doc2Doc needs a way to restore documents from saved backups. However, not all original documents may have backups, and some backups might be corrupted.

Assignment
Complete the restore_documents function in one line - if you can. It takes two tuples of document strings, originals and backups, as input and returns a set.

Convert all documents to the same case with .upper() for comparison.
Filter out documents that are corrupted strings of random numbers with .isdigit().
Return the combined originals and backups tuples, removing any duplicates using a set.

"""


def restore_documents(originals, backups):
    return set(filter(lambda item: not item.isdigit(), map(lambda item: item.upper(),originals + backups)))
