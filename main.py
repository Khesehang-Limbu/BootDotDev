"""

Copy/Paste
Doc2Doc has a simple clipboard for copying to and pasting from a cache. Initialize the clipboard to set and get strings.

Assignment
Complete the new_clipboard function. It accepts a dictionary as input and returns two functions, copy_to_clipboard and paste_from_clipboard. It should not modify the original input dictionary.

copy_to_clipboard: It takes a key and value string pair and adds them to the clipboard dictionary.
paste_from_clipboard: It takes a key string and returns its value from the clipboard dictionary. If the key is missing from the clipboard, return an empty string.

"""


def new_clipboard(initial_clipboard):
    # ?
    clipboard_copy = initial_clipboard.copy()

    def copy_to_clipboard(key, value):
        clipboard_copy.update({key: value})

    def paste_from_clipboard(key):
        return clipboard_copy[key] if key in clipboard_copy.keys() else ""

    return copy_to_clipboard, paste_from_clipboard
