"""

No-Op
A no-op is an operation that does... nothing.

If a function doesn't return anything, it's probably impure. If it doesn't return anything, the only reason for it to exist is to perform a side effect.

Example No-Op
This function performs a useless computation because it doesn't return anything or perform a side-effect. It's a no-op.

def square(x):
    x * x

Example Side-Effect
This function performs a side effect. It changes the value of the y variable that is outside of its scope. It's impure.

y = 5
def add_to_y(x):
    global y
    y += x

add_to_y(3)
# y = 8

The global keyword just tells Python to allow access to the outer-scoped y variable.

print()
Even the print() function (technically) has an impure side effect! It doesn't return anything, but it does print text to the console, which is a form of i/o.

Assignment
Complete the remove_emphasis, remove_emphasis_from_line, and remove_emphasis_from_word functions. They are currently no-ops.

remove_emphasis is the parent function. It takes a full document with any number of lines and removes any single or double * characters that are at the start or end of a word. (Emphasis in markdown)

For example, this:

I *love* markdown.
I **really love** markdown.

Should become:

I love markdown.
I really love markdown.

Write the helper functions, they will make the remove_emphasis function much easier to write:

The remove_emphasis_from_word function should remove emphasis from a single word.
The remove_emphasis_from_line function should split a given line into words and use the function we just created to remove emphasis from each word.
Don't forget to handle newline characters (\n) appropriately at the end of lines.

"""


def remove_emphasis_from_word(word):
    # ?
    if word == "":
        return word

    if word[0] == "*" and word[1] == "*" and word[-1] == "*" and word[-2] == "*":
        word = word[2:len(word)-2:]
    elif word[0] == "*" and word[1] == "*":
        word = word[2::]
    elif word[-1] == "*" and word[-2] == "*":
        word = word[:len(word)-2:]

    if word[0] == "*" and word[-1] == "*":
        word = word[1:len(word)-1:]
    elif word[0] == "*":
        word = word[1::]
    elif word[-1] == "*":
        word = word[:len(word)-1:]

    return word


def remove_emphasis_from_line(line):
    return " ".join(list(map(remove_emphasis_from_word, line.split(" "))))


def remove_emphasis(doc_content):
    return "\n".join(map(remove_emphasis_from_line, doc_content.split("\n")))
