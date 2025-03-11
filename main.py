"""

Toggle Case
We need to add a feature to Doc2Doc that switches the capitalization of all the words in a line.

Assignment
Complete the toggle_case function using string methods. It takes a string as input line, and returns a string.

If line is in titlecase, convert it to all uppercase and add three "!" to the end.
If line is all uppercase, convert it to all lowercase except for the first letter and remove all trailing "!".
If line is all lowercase or only the first letter is capitalized, convert it to title case.
Otherwise, just return line unchanged.

"""


def toggle_case(line):
    if line.istitle():
        return f"{line.upper()}!!!"
    if line.isupper():
        return f"{line[0].upper()}{line[1::].lower().replace("!", "")}"
    if len(line) > 0 and line[1:].islower():
        return line.title()
    return line
