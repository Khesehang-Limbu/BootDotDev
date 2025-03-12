"""

Longest Word
In Doc2Doc, we have a search function to find the longest word in a document.

Assignment
Complete the find_longest_word function without a loop. It accepts string inputs, document, and optional longest_word, which is the current longest word and defaults to an empty string.

Check if the first word is longer than the current longest_word, then recur for the rest of the document.
Ensure there are no potential index errors.
Assume that a "word" means a series of any consecutive non-whitespace characters. For example, longest_word("How are you?") should return the string "you?".

"""


def find_longest_word(document, longest_word=""):
    word_documents = document.split(" ")

    if document == "":
        return longest_word

    if len(word_documents) == 1 and len(word_documents[0]) > len(longest_word):
        longest_word = word_documents[0]

    if len(word_documents[0]) > len(longest_word):
        longest_word = word_documents[0]

    longest_word = find_longest_word(
        ' '.join(word_documents[1::]), longest_word)

    return longest_word
