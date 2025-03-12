"""

CSS Styles
Doc2Doc should be able to add css styling to an html file. CSS uses selectors to identify the html element to add the style property. Essentially, styles are a chain of keys and values.

Assignment
Complete the css_styles function. It accepts a nested dictionary as input, initial_styles, and returns a function, add_style.

Copies initial_styles to avoid modifying the original dictionary.
Returns an add_style function that:
Takes three string arguments: selector, property, and value. selector is a key in the initial_styles dictionary and its value should be a dictionary.
Checks if the selector exists in the dictionary. If not, creates a new dictionary for the selector value.
Then adds or updates the property with the given value for the selector.
Returns the updated dictionary.
For example:

initial_styles = {
    "body": {
        "background-color": "white",
        "color": "black"
    },
    "h1": {
        "font-size": "16px",
        "padding": "10px"
    }
}

add_style = css_styles(initial_styles)

new_styles = add_style("p", "color", "grey")
# {
#    "body": {
#        "background-color": "white",
#        "color": "black"
#    },
#    "h1": {
#        "font-size": "16px",
#        "padding": "10px"
#    },
#    "p": {
#        "color": "grey",
#    }
# }

"""


def css_styles(initial_styles):
    new_styles = initial_styles.copy()

    def add_style(selector, property, value):
        if selector not in new_styles.keys():
            new_styles[selector] = {
                property: value,
            }
        else:
            if isinstance(new_styles[selector], dict):
                new_styles[selector].update({
                    property: value,
                })
        return new_styles
    return add_style
