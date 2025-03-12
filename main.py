"""

Count Nested Levels
In Doc2Doc, we might have documents nested inside other documents, forming a kind of tree. You know how crazy .docx files can get...

Anyways, we want to find out how deeply nested a given document is.

Assignment
Complete the count_nested_levels function.

Loop over document_ids in the nested_documents dictionary
If the current document_id matches the target_document_id, return its level of nesting
If the target_document_id is not found, recursively call count_nested_levels on the current document_id and increment the level
If it found the target_document_id's level, return it
If the target_document_id doesn't exist, the function should return -1
Example
In this dictionary, the document with id 3 is nested 2 levels deep. Document 2 is nested 1 level deep.

{
    1: {
        3: {}
    },
    2: {}
}

"""


def count_nested_levels(nested_documents, target_document_id, level=1):
    for id in nested_documents.keys():
        if id == target_document_id:
            return level
        else:
            current_level = count_nested_levels(
                nested_documents[id], target_document_id, level+1)
            if current_level != -1:
                return current_level
    return -1
