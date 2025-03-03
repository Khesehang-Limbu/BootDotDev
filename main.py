"""
Purchasing
Now we need to use our purchase_item function to process an entire list of character purchases.

Assignment
Complete the process_transactions function. It takes a list of purchase orders. Each order is a dictionary. Look through the main() function to see the shape of this data.

First, create an empty list of leftovers.

Then, loop over the list of purchase orders.

For each order in the provided list, try to process the order with the purchase_item function. If an exception is raised, catch it and print the error message.

If the purchase was successful. Append the remaining money to the leftovers list. If there is an error, do not add anything to the leftovers.

Be sure to loop over the entire list of purchase orders.

Finally, after the loop has ended, return the leftovers list.

You must keep the same order of purchases, but with the unsuccessful purchases removed.

Remember to remove any extra print statements you added for debugging before submitting the lesson!
"""
def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    return gold_available - price

def process_transactions(purchase_orders):
    leftovers = []
    for order in purchase_orders:
        try:
            leftover = purchase_item(order["price"], order["gold_available"])
            leftovers.append(leftover)
        except Exception as e:
            print(e)
    return leftovers

# Don't edit below this line


def main():
    print("Processing transactions...")
    leftovers = process_transactions(
        [
            {"price": 10.00, "gold_available": 125.00},
            {"price": 5.00, "gold_available": 2.00},
            {"price": 20.01, "gold_available": 5.20},
            {"price": 1.04, "gold_available": 254.00},
            {"price": 40.20, "gold_available": 6.00},
            {"price": 16.00, "gold_available": 235.01},
            {"price": 10.70, "gold_available": 10.70},
            {"price": 12.00, "gold_available": 2.30},
        ]
    )
    print("Transactions complete!")
    print("Leftover amounts for successful purchases:")
    for leftover in leftovers:
        print(f" * {leftover:.2f}")

main()
