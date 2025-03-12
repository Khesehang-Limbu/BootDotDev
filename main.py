"""

Match
Let's take another look at our example Enum from the previous lesson:

Color = Enum("Color", ["RED", "GREEN", "BLUE"])

Working With Enums
Python has a match statement that tends to be a lot cleaner than a series of if/else/elif statements when we're working with a fixed set of possible values (like a sum type, or more specifically an enum):

def get_hex(color):
    match color:
        case Color.RED:
            return "#FF0000"
        case Color.GREEN:
            return "#00FF00"
        case Color.BLUE:
            return "#0000FF"

        # default case
        # (invalid Color)
        case _:
            return "#FFFFFF"

If you have two values to match, you can use a tuple:

def get_hex(color, shade):
    match (color, shade):
        case (Color.RED, Shade.LIGHT):
            return "#FFAAAA"
        case (Color.RED, Shade.DARK):
            return "#AA0000"
        case (Color.GREEN, Shade.LIGHT):
            return "#AAFFAA"
        case (Color.GREEN, Shade.DARK):
            return "#00AA00"
        case (Color.BLUE, Shade.LIGHT):
            return "#AAAAFF"
        case (Color.BLUE, Shade.DARK):
            return "#0000AA"

        # default case
        # (invalid combination)
        case _:
            return "#FFFFFF"

The value we want to compare is set after the match keyword, which is then compared against different cases/patterns. If a match is found, the code in the block is executed.

Assignment
Complete the convert_format function. Using the enum DocFormat, it should support 3 types of conversions:

From MD to HTML:

Assume the content is a single h1 tag in markdown syntax - it's a single string representing a line. Replace the leading # with an <h1> and add a </h1> to the end.

# This is a heading -> <h1>This is a heading</h1>

From TXT to PDF:

Simply add a [PDF] tag to the beginning and end of the content. Notice the spaces between [PDF] tags and the content:

This is some text -> [PDF] This is some text [PDF]

From HTML to MD:

Replace any <h1> tags with # and remove any </h1> tags.

<h1>This is a heading</h1> -> # This is a heading

Any other conversion:

If the input format is invalid, raise an Exception with the string invalid type.

"""

from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# don't touch above this line


def convert_format(content, from_format, to_format):
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            return content.replace("# ", "<h1>") + "</h1>"
        case (DocFormat.TXT, DocFormat.PDF):
            return f"[PDF] {content} [PDF]"
        case (DocFormat.HTML, DocFormat.MD):
            return content.replace("<h1>", "# ").replace("</h1>", "")
        case _:
            raise Exception("invalid type")

