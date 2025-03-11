"""

What Is Functional Programming?
Functional programming is a style (or "paradigm" if you're pretentious) of programming where we compose functions instead of mutating state (updating the value of variables).

Functional programming is more about declaring what you want to happen, rather than how you want it to happen.
Imperative (or procedural) programming declares both the what and the how.
Example of imperative code:

car = create_car()
car.add_gas(10)
car.clean_windows()

Example of functional code:

return clean_windows(add_gas(create_car()))

The important distinction is that in the functional example, we never change the value of the car variable, we just compose functions that return new values, with the outermost function, clean_windows in this case, returning the final result.

Doc2Doc
In this course, we're working on "Doc2Doc", a command line tool for converting documents from one format to another. If you're familiar with Pandoc, the idea is similar.

Assignment
Complete the stylize_title function. It should take a single string as input, and return a single string as output. The returned string should have both the title centered and a border added.

Use the provided functions center_title and add_border.
Center the title before adding the border.
Do not create any variables.
Use only 1 line of code in the function body.

"""


def stylize_title(document):
    return add_border(center_title(document))


# Don't touch below this line


def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)
