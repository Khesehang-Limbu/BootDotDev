"""

Join Strings
Write a function called join_strings() that takes a list of strings and returns a single string. Concatenate the strings from the list end-to-end, in order, with a comma between them. Don't use the .join() string method.

Example
string_list = ["hello", "my", "friend"]
joined_string = join_strings(string_list)
print(joined_string) # "hello,my,friend"

"""

def join_strings(strings):
    new_string = ""
    for i in range(len(strings)):
        if i != len(strings) - 1:
            new_string += strings[i] + ","
        else:
            new_string += strings[i]
    return new_string
