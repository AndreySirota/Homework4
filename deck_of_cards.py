"""Homework 13: deck_of_cards"""


import random


class Card:
    """class Card"""
    number_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    mast_list = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self, number, mast):
        """Constructor class Card"""
        self.number = number
        self.mast = mast

    def __str__(self):
        """Function __str__"""
        return f'{self.mast} {self.number}'

    def is_joker(self):
        """is_joker"""
        return self.number == "Joker" or self.mast is None


class CardsDeck:
    """class CardsDeck"""

    def __init__(self):
        """Constructor class CardsDeck"""
        self.cards = []
        for mast in Card.mast_list:
            for number in Card.number_list:
                self.cards.append(Card(number, mast))
        self.cards.append("Joker1")
        self.cards.append("Joker2")

    def shuffle(self):
        """Function shuffle"""
        random.shuffle(self.cards)

    def get(self, index):
        """Function get"""
        if 1 <= index <= len(self.cards):
            return self.cards.pop(index-1)
        return False


deck = CardsDeck()
deck.shuffle()
card_number = int(input('Choose a card from a deck of 54 cards:'))
card = deck.get(card_number)
print(f'You card is: {card}')
card_number = int(input('Choose a card from a deck of 54 cards:'))
card = deck.get(card_number)
print(f'You card is: {card}')
