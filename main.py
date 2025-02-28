"""
Alchemy Ingredients
Fantasy Quest added a new alchemy profession, users would like a way to know how many ingredients they have compared to the required ingredients in their recipes.

Assignment
Finish the check_ingredient_match function by looping over the recipe list. The function should calculate and return a percentage of ingredients the character has, as well as a list of missing from the recipe.

For example, if these were the lists:

recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
ingredients = ["Dragon Scale", "Goblin Ear", "Phoenix Feather", "Troll Tusk"]

percentage, missing_ingredients = check_ingredient_match(recipe, ingredients)
print(percentage, missing_ingredients)
# Prints: 75.00 ["Unicorn Hair"]
"""

def check_ingredient_match(recipe, ingredients):
    missing_ingredients = []
    ingredient_count = 0

    for item in recipe:
        if item not in ingredients:
            missing_ingredients.append(item)
        else:
            ingredient_count += 1

    return (ingredient_count/len(ingredients))*100, missing_ingredients



