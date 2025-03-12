"""

Currying
Function currying is a specific kind of function transformation where we translate a single function that accepts multiple arguments into multiple functions that each accept a single argument.

This is a "normal" 3-argument function:

box_volume(3, 4, 5)

This is a "curried" series of functions that does the same thing:

box_volume(3)(4)(5)

Here's another example that includes the implementations:

def sum(a, b):
  return a + b

print(sum(1, 2))
# prints 3

And the same thing curried:

def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum

print(sum(1)(2))
# prints 3

The sum function only takes a single input, a. It returns a new function that takes a single input, b. This new function when called with a value for b will return the sum of a and b. We'll talk later about why this is useful.

Assignment
In Doc2Doc, depending on the type of text file we're working with, we sometimes need to transform the font size of the text when it comes time to render it on the screen.

Fix the converted_font_size function. We are using a 3rd party code library that expects our function to be a curried series of functions that each take a single argument.

converted_font_size should just take a single argument, font_size and return a function that takes a single argument, doc_type. That function should return the font_size multiplied by the appropriate value for the given doc_type.

"""


def converted_font_size(font_size):
    def inner_func(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("invalid doc type")
    return inner_func
