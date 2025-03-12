"""

Decorators
The *args and **kwargs syntax is great for decorators that are intended to work on functions with different signatures.

Example
The log_call_count function below doesn't care about the number or type of the decorated function's (func_to_decorate) arguments. It just wants to count how many times the function is called. However, it still needs to pass any arguments through to the wrapped function.

def log_call_count(func_to_decorate):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Called {count} times")
        # The * and ** syntax unpacks the arguments
        # and passes them to the decorated function
        return func_to_decorate(*args, **kwargs)

    return wrapper

Assignment
Complete the markdown_to_text_decorator function. It can decorate a function with any number of string arguments, no matter if they're positional or keyword args. It will run the decorated function, but first strip out any Markdown heading symbols (see below for an explanation of Markdown headings).

It should return a wrapper function that takes *args and **kwargs. The wrapper should:

Map the *args to a new list where each string is converted to plain text using convert_md_to_txt.
Map the **kwargs to a new dictionary where each "value" is converted to plain text using convert_md_to_txt. The "key" should remain the same.
Use the .items() dictionary method to pass a list of tuples of key-value pairs to map
Create a function for map which changes the value of an item tuple with convert_md_to_txt
Return the result of calling the decorated function with the new arguments.

"""


def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        plain_text_list = list(map(convert_md_to_txt, args))
        plain_text_for_dict = list(map(plain_text_dict, kwargs.items()))
        new_args = plain_text_list + plain_text_for_dict
        return func(*new_args)

    return wrapper


def plain_text_dict(item):
    return convert_md_to_txt(item[1])


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
