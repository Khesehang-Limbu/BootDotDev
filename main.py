"""

Enums
Doing the admittedly weird class and isinstance() thing works, but it turns out, there's a better way in some cases. If you're trying to represent a fixed set of values (but not store additional data within them) enums are the way to go.


Let's say we have a Color variable that we want to restrict to only three possible values:

RED
GREEN
BLUE
We could use a plain-old string to represent these values, but that's annoying because we have to remember all the "valid" values and defensively check for invalid ones all over our codebase. Instead, we can use an Enum:

from enum import Enum

Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
print(Color.RED)  # this works, prints 'Color.RED'
print(Color.TEAL) # this raises an exception

Now Color is a sum type! At least, as close as we can get in Python.

There are a few benefits:

A "Color" can only be RED, GREEN, or BLUE. If you try to use Color.TEAL, Python raises an exception.
There is a central place to see the "valid" values for a Color.
Each "Color" has a "name" (e.g. Color.RED) and a "value" (e.g. 1). The value is an integer and is used under the hood instead of the name. Integers take up less memory than strings, which helps with performance.
Assignment
Create an Enum called Doctype with values:

PDF
TXT
DOCX
MD
HTML

"""

from enum import Enum

Doctype = Enum("Doctype", ["PDF", "TXT", "DOCX", "MD", "HTML"])
