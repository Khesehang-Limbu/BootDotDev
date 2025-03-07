"""

Deck of Cards
Assignment
Finish the DeckOfCards class. The SUITS and RANKS of each card have been provided for you as class variables. You won't need to modify them, but you will need to use them.

Constructor
Initialize a private empty list called cards.
Fill that empty list by calling the create_deck method within the constructor.
create_deck(self)
This method should create a (Rank, Suit) tuple for all 52 cards in the deck and append them to the cards list.

Order matters! The cards should be appended to the list in the following order: all ranks of hearts, then diamonds, then clubs, and finally spades. Within each suit, the cards should be ordered from lowest rank (Ace) to highest rank (King).

shuffle_deck(self)
This method should use the random.shuffle() method (available from the random package) to shuffle the cards in the deck.

deal_card(self)
This method should .pop() the first card off the top of the deck (top of the deck is the end of the list) and return it. If there are no cards left in the deck the method should instead return None.

"""

import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for suit in DeckOfCards.SUITS:
            for rank in DeckOfCards.RANKS:
                self.__cards.append((rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if len(self.__cards) == 0:
            return None
        last_card = self.__cards.pop()
        return last_card

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
