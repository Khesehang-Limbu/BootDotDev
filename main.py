"""

Escape HTML
You can stack decorators, and you can use currying with decorators.

def to_uppercase(func):
    def wrapper(document):
        return func(document.upper())

    return wrapper

def get_truncate(length):
    def truncate(func):
        def wrapper(document):
            return func(document[:length])

        return wrapper

    return truncate

@to_uppercase
@get_truncate(9) # currying
def print_input(input):
    print(input)

print_input("Keep Calm and Carry On")
# prints: "KEEP CALM"

Observe that to_uppercase wrapped get_truncate(9), and get_truncate(9) returned truncate which wrapped print_input, then print_input printed "KEEP CALM" from "Keep Calm and Carry On".

You might not know anything about HTML. That's fine. This challenge isn't about HTML directly. Just understand that it's a markup language like markdown. Certain characters are interpreted as part of HTML tags. In order to show these characters without interpreting them, they must be encoded as escape sequences. tldr: replace "<" with "&lt;".

Doc2Doc needs a feature that can take care of encoding such characters for you. This is particularly helpful if you want to show raw HTML on a vanilla HTML webpage. HTML even has a semantic <pre> tag for designating pre-formatted text.

Assignment
Complete the replacer function.

It takes as input two strings, old and new, and returns a function, replace.
replace takes an input function, decorated_func, and returns a wrapper function.
wrapper takes as input a string text. It uses .replace() string method to replace instances of old with new in the text. Then it returns the result of passing the modified text to the decorated_func.
Use a series of the replacer function to decorate tag_pre. Pass the following pairs of strings to these decorators to encode the escape sequences:
Replace "&" with "&amp;"
Replace "<" with "&lt;"
Replace ">" with "&gt;"
Replace '"' with "&quot;"
Replace "'" with "&#x27;"

"""


def replacer(old, new):
    def replace(decorated_func):
        def wrapper(text):
            modified_text = text.replace(old, new)
            return decorated_func(modified_text)
        return wrapper
    return replace


@replacer("&", "&amp;")
@replacer("'", "&#x27;")
@replacer('"', "&quot;")
@replacer(">", "&gt;")
@replacer("<", "&lt;")
def tag_pre(text):
    return f"<pre>{text}</pre>"

