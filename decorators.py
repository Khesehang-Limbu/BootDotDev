"""

Configure Plugin
Doc2Doc should be extensible to allow for third-party plugins. These plugins will be configurable.

Assignment
Complete the configure_plugin_decorator function. It decorates a func that takes keyword arguments **kwargs, but the wrapper function it returns takes positional arguments *args. The arguments passed to the wrapper will be a series of tuples, each a key/value pair.

Convert the args into a dictionary with the dict function.
Get the result of passing this dictionary into the func as keyword arguments unpacked with the ** operator.
Return the result.
plugin_config = configure_backups(("path", "~/duplicates"), ("prefix", "duplicate_"), ("extension", ".rtf"))

# plugin_config:
# {
#   "path": "~/duplicates",
#   "prefix": "duplicate_",
#   "extension": ".rtf",
# }

"""


def configure_plugin_decorator(func):
    def wrapper(*args):
        dict_args = dict(args)
        return func(**dict_args)
    return wrapper
