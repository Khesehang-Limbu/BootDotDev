"""

Args and Kwargs
In Python, *args and **kwargs allow a function to accept and deal with a variable number of arguments.

*args collects positional arguments into a tuple
**kwargs collects keyword (named) arguments into a dictionary
def print_arguments(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print_arguments("hello", "world", a=1, b=2)
# Positional arguments: ('hello', 'world')
# Keyword arguments: {'a': 1, 'b': 2}

Positional Arguments
Positional arguments are the ones you're already familiar with, where the order of the arguments matters. Like this:

def sub(a, b):
    return a - b

# a=3, b=2
res = sub(3, 2)
# res = 1

Keyword Arguments
Keyword arguments are passed in by name. Order does not matter. Like this:

def sub(a, b):
    return a - b

res = sub(b=3, a=2)
# res = -1
res = sub(a=3, b=2)
# res = 1

A Note on Ordering
Any positional arguments must come before keyword arguments. This will not work:

sub(b=3, 2)

Assignment
At Doc2Doc, we need better internal debugging tools. Complete the args_logger function. It takes a variable number of positional and keyword arguments and prints them to the console.

Print each positional argument sequentially using numbers and periods as the prefixes, starting with 1.. For example:
args_logger("what's", "up", "doc")

prints to the console:

1. what's
2. up
3. doc

Print each keyword argument alphabetically by key using asterisks (*) as the prefix with a colon (:) in between. For example:
args_logger("hi", "there", age=17, date="July 4 1776")

prints to the console:

1. hi
2. there
* age: 17
* date: July 4 1776

Use the sorted() function to get the order right.

"""


def log_to(*args, **kwargs):
    def wrapper(*args, **kwargs):
        for i in range(len(args)):
            print(f"{i+1}. {args[i]}")

        for key in sorted(kwargs):
            print(f"* {key}: {kwargs[key]}")
    return wrapper


@log_to
def args_logger(*args, **kwargs):
    # ?
    pass


def test(*args, **kwargs):
    args_logger(*args, **kwargs)
    print("========================================")


def main():
    test("Good", "riddance", date_str="01/01/2023")
    test(message="Hello World", to_delete="l")
    test("two", "star-crossed", "lovers")
    test("hi", True, f_name="Lane", l_name="Wagner", age=28)


main()
