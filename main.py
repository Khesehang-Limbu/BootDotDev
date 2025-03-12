"""

Markdown Image
Markdown makes displaying images as simple as possible. To add an image to a markdown document, just use this syntax:

![alt text](url "title")

alt text a brief description for screen readers and web scrapers. Required for accessibility.
url url or relative path to image.
title shown on mouse hover. Optional.
Assignment
Doc2Doc makes using markdown a breeze. This includes adding images to markdown documents.

Complete the create_markdown_image function using currying. It takes a string input, alt_text, and returns an inner function.
It should enclose the alt_text in square brackets prefixed with an exclamation point ![alt_text].
Create the inner function returned by create_markdown_image. It also takes a string input, url, and returns an innermost function.
The inner function should first escape any parentheses in the URL by replacing them with encoded sequences.
Use the .replace() string method to change any opening parenthesis ( into %28.
Do the same to change any closing parenthesis ) into %29.
Enclose the url with parentheses (url).
Add the enclosed url to the end of the enclosed alt_text: ![alt_text](url)
Create the innermost function returned by the inner function. It should take an optional string input for the title.
If a title is passed:
Enclose it in double quotes.
Then add the quoted title to the image syntax by first removing the closing parenthesis ) from the end of the image syntax.
Add a space and the quoted title with a closing parenthesis ) to the end of the image syntax: ![alt_text](url "title")
Return the finished image syntax.

"""


def create_markdown_image(alt_text):
    alt_text = f"![{alt_text}]"

    def create_image_url(url):
        url = url.replace("(", "%28")
        url = url.replace(")", "%29")
        url = f"({url})"

        def create_image_title(title=""):
            if title != "":
                title = f' "{title}")'
                nonlocal url
                url = url.replace(")", title)
            return alt_text + url
        return create_image_title
    return create_image_url
