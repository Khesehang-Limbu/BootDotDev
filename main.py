"""

Decorators
Python decorators are just syntactic sugar for higher-order functions.

Example:

def vowel_counter(func_to_decorate):
    vowel_count = 0
    def wrapper(doc):
        nonlocal vowel_count
        vowels = "aeiou"
        for char in doc:
            if char in vowels:
                vowel_count += 1
        print(f"Vowel count: {vowel_count}")
        return func_to_decorate(doc)
    return wrapper

@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")

process_doc("What")
# Vowel count: 1
# Document: What

process_doc("a wonderful")
# Vowel count: 5
# Document: a wonderful

process_doc("world")
# Vowel count: 6
# Document: world

The @vowel_counter line is "decorating" the process_doc function with the vowel_counter function. vowel_counter is called once when process_doc is defined with the @ syntax, but the wrapper function that it returns is called every time process_doc is called. That's why vowel_count is preserved and printed after each time.

It's Just Syntactic Sugar
Python decorators are just another (sometimes simpler) way of writing a higher-order function. These two pieces of code are identical:

With Decorator
@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")

process_doc("Something wicked this way comes")

Without Decorator
def process(doc):
    print(f"Document: {doc}")

process_doc = vowel_counter(process)
process_doc("Something wicked this way comes")

Assignment
The provided file_type_aggregator function is intended to decorate other functions. It assumes that the function it decorates has exactly 2 positional arguments.

Create a process_doc function that's decorated by file_type_aggregator. It should return the following string:

f"Processing doc: '{doc}'. File Type: {file_type}"

Where doc and file_type are its positional arguments. (See line 11 for where it's being called)

"""


def file_type_aggregator(func_to_decorate):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper


# don't touch above this line

# ?
@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: '{doc}'. File Type: {file_type}"

