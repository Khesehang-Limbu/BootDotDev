"""
""Counting Practice
Checking for Existence
If you're unsure whether or not a key exists in a dictionary, use the in keyword.

cars = {
    "ford": "f150",
    "toyota": "camry"
}

print("ford" in cars)
# Prints: True

print("gmc" in cars)
# Prints: False

Assignment
We need to be able to report to our players how many enemies are in their immediate vicinity - but they want the count of each enemy by its kind.

If you run the code, it will result in a KeyError.

Fix the count_enemies function. It takes a list of enemy_names as input. It should return a dictionary where the keys are all the enemy names from the list, and the values are the counts of how many times each enemy appeared in the list.
"""

def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict.keys():
            enemies_dict[enemy_name] = enemies_dict[enemy_name] + 1
        else:
            enemies_dict[enemy_name] = 1
    return enemies_dict
