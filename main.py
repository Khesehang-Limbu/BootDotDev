"""
Purchasing
There's a bug in the current vendor system that is letting players buy items from the shop even when they don't have enough gold.

Assignment
Complete the purchase_item function. If the character doesn't have enough gold raise an exception with the text not enough gold. Don't handle the exception.

Otherwise, return the amount of money the customer has leftover after completing the purchase.
"""
def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    return gold_available - price
