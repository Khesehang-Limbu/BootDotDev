"""
Iterating Over a Dictionary in Python
We can iterate over a dictionary's keys using the same no-index syntax we used to iterate over the values in a list. With access to the dictionary's keys, we also have access to their corresponding values.

fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny

Note: we could have just as easily set the name variable to key or simply k.

Assignment
We need to display on our player's screens what the most common enemy in a given area of the game map is.

Complete the get_most_common_enemy function by iterating over all enemies in the dictionary and returning only the name of the enemy with the highest count.

If there are no enemies, return a None value. If there are multiple enemies with the same highest count, return the first one found.

enemies_dict is a dictionary of name -> count. Example:

{
    "jackal": 1,
    "kobold": 2,
    "soldier": 3,
    "gremlin": 5
}

Tip: Negative Infinity
When you're trying to find a "max" value, it helps to keep track of the "max so far" in a variable and to start that variable at the lowest possible number, negative infinity.

max_so_far = float("-inf")

You'll also want to keep track of the enemy name associated with the maximum count. I would set the default for that variable to None.
"""

def get_most_common_enemy(enemies_dict):
    max = float("-inf")
    name = None

    for k,v in enemies_dict.items():
        if v > max:
            max = v
            name = k
    return name
