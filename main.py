"""
Evens and Odds
You've been asked to write a program that will calculate how many odd and even numbers exist in a list.

Challenge
Write the get_odds_and_evens function to loop through the numbers list and check if each number in the list is either odd or even.

Increment the num_evens counter if even, and the num_odds counter if it's odd. Lastly, return the two values num_odds and num_evens in that order.
"""

def get_odds_and_evens(numbers):
    num_odds = 0
    num_evens = 0

    # Don't touch above this line
    for num in numbers:
        if num % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1
    return num_odds, num_evens


