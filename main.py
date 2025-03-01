"""
Vendor
Fantasy Quest players want a way to track what items they purchased from the vendor, how much it cost, and what they still need to purchase from their tracked items list.

Assignment
Complete the calculate_total function.

Inputs
items_purchased: A list of the names of items purchased. This is a list of strings.
pinned_list: A list of the names of items the player has 'pinned' and wanted to purchase. This is also a list of strings.
Outputs
The function should return 3 values in this order:

unpurchased_items: A list of all the item names in pinned_list that weren't found in items_purchased, in the same order that they originally appeared in the pinned_list.
receipt: A dictionary containing all the items the player purchased, even stuff not on their pinned_list. The keys are the item names and the values are their respective prices from the item_prices dictionary.
total_cost: The total cost of all the items that were purchased.
Return each value separately, not in a singular list. For example:

return value1, value2, value3
"""

def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    # Don't touch above this line
    receipt = {}
    total = 0
    unpurchased_items = []

    for item in items_purchased:
        receipt[item] = item_prices[item]
        total += item_prices[item]

    for item in pinned_list:
        if not item in items_purchased:
            unpurchased_items.append(item)

    return unpurchased_items, receipt, total


#print(
#    calculate_total(
#            [
#                "health_potion",
#                "mana_potion",
#                "gold_dust",
#                "herbs",
#                "crystal_shard",
#                "dwarven_ale",
#            ],
#            [
#                "health_potion",
#                "mana_potion",
#                "ice_cold_milk",
#                "gold_dust",
#                "herbs",
#                "crystal_shard",
#                "magic_ring",
#                "dwarven_ale",
#                "mystic_amulet",
#            ],
#
#    )
#)



