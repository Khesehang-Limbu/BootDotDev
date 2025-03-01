"""
"Duplicate Keys
Because dictionaries rely on unique keys, you can't have two of the same key in the same dictionary. If you try to use the same key twice, the first value will simply be overwritten.

Assignment
Another developer on our team has introduced a bug by specifying duplicate keys in the dictionary! Fix the bug.

The get_character_record function takes a character's name, server, level, and rank. It should return a dictionary with the following fields:

name
server
level
rank
id
Where the id is the name and the server concatenated together with a # in the middle for uniqueness. We can't have two bloodwarrior123's on the same server!
"""

def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }

