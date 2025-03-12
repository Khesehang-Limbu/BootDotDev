"""

Upgrade Filter Command
Users like the filter command, but think it could be better. They want access to more than two filter options and to customize the words that get filtered. It's time to upgrade the filter command feature.

Assignment
Complete the get_filter_cmd function. It should take a dictionary as input, filters, and return a function, filter_cmd.
filters contains option string and filter function key/value pairs.
filter_cmd should take as input a string content to be filtered, a list of strings options, and a list of tuples word_pairs.
The filter_cmd should filter and return the content, filtered according to the input options
If there are no options in the options list, raise an exception "missing options".
For each option, if its option string is in the filters dictionary, then filter the content by passing the content and word_pairs to the option's filter.
Raise an exception "invalid option" for any option that is passed but not found in the filters dictionary.

"""


def get_filter_cmd(filters):
    def filter_cmd(content, options, word_pairs):
        if len(options) == 0:
            raise Exception("missing options")
        for option in options:
            try:
                content = filters[option](content, word_pairs)
            except Exception:
                raise Exception("invalid option")
        return content
    return filter_cmd


# don't touch below this line


def replace_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[1])
    return content


def remove_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], "")
    return content


def capitalize_sentences(content, word_pairs):
    return ". ".join(map(str.capitalize, content.split(". ")))


def uppercase_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[0].upper())
    return content


filters = {
    "--replace": replace_words,
    "--remove": remove_words,
    "--capitalize": capitalize_sentences,
    "--uppercase": uppercase_words,
}
