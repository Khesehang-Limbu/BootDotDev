"""

Edit Document
Doc2Doc should be able to track changes in documents. Tracking changes is important for undoing and redoing edits. Some editors save changes and some file formats do as well.

Assignment
Complete the handle_edit function. It takes as input a document string, an edit_type EditType enum, and an edit dictionary. It should use a match case statement to select the correct operation depending on the EditType. Create a function to handle each operation as follows:

NEWLINE:
Use the edit dictionary to modify and return a copy of the document. The edit dictionary will only contain a line_number key and integer value (zero-indexed!). Add a newline \n at the end of the line of the document corresponding to the line_number.

SUBSTITUTE:
Use the edit dictionary to modify and return a copy of the document. The edit dictionary will contain a insert_text key and string value, a line_number key and integer value, a start key and integer value and an end key and integer value. Substitute the insert_text into the line of the document corresponding to the line_number between the start and end indexes.

INSERT:
Use the edit dictionary to modify and return a copy of the document. The edit dictionary will contain a insert_text key and string value, a line_number key and integer value, and a start key and integer value. Insert the insert_text into the line of the document corresponding to the line_number at the start index.

DELETE:
Use the edit dictionary to modify and return a copy of the document. The edit dictionary will contain a line_number key and integer value, a start key and integer value, and an end key and integer value. Remove the substring of the line of the document corresponding to the line_number between the start and end indexes.

Exceptions:
If the edit_type is none of the above, raise an Exception with the string "unknown edit type".


"""


from enum import Enum


class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4


def handle_edit(document, edit_type, edit):
    match edit_type:
        case EditType.NEWLINE:
            document_copy = document
            lines = document_copy.split("\n")
            for index in range(len(lines)):
                if index == edit["line_number"]:
                    lines[index] += "\n"
            return "\n".join(lines)
        case EditType.SUBSTITUTE:
            lines = document.split("\n")
            for index in range(len(lines)):
                if index == edit["line_number"]:
                    to_replace = lines[index][edit["start"]:edit["end"]:]
                    lines[index] = lines[index].replace(to_replace, edit["insert_text"])
            return "\n".join(lines)
        case EditType.INSERT:
            lines = document.split("\n")
            for index in range(len(lines)):
                if index == edit["line_number"]:
                    lines[index] = lines[index][:edit["start"]:] + edit["insert_text"] + lines[index][edit["start"]::]
            return "\n".join(lines)
        case EditType.DELETE:
            lines = document.split("\n")
            for index in range(len(lines)):
                if index == edit["line_number"]:
                    lines[index] = lines[index].replace(lines[index][edit["start"]:edit["end"]:], "")
            return "\n".join(lines)
        case _:
            raise Exception("unknown edit type")

