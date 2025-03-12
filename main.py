"""

Line Breaking
Users should be able to break lengthy text into manageable lines. Lineation is simply dividing text into lines. This concept can also be applied to other data structures, such as code blocks or formatted paragraphs.

Assignment
Complete the inner add_word_to_lines function. It takes a list of strings, lines, and a string word, as inputs and returns lines with the word added.

If lines is empty, return just word in a list
Assign the last line in lines to current_line
If the length of current_line and word plus one (for a space) is more than line_length, start a new line by appending word to lines
Else, add word to current_line with a space, and assign the new string to the last index in lines
Remember to return lines
Note: Every line will have at least one word, even if that word is longer than the line_length.

lineate = lineator(11)
lines = lineate("Boots loves salmon because he is a bear.")
# lines: ["Boots loves", "salmon", "because he", "is a bear."]

"""


from functools import reduce


def lineator(line_length):
    def lineate(document):
        words = document.split()

        def add_word_to_lines(lines, word):
            # ?
            if len(lines) == 0:
                return [word]

            current_line = lines[-1]

            if len(current_line) + len(word) + 1 > line_length:
                lines.append(word)
            else:
                current_line += f" {word}"
                lines[-1] = current_line
            return lines

        return reduce(add_word_to_lines, words, [])

    return lineate

