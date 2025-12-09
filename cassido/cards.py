#!/usr/bin/env python3
"""This week's (2025-12-08) question:Make a data structure for a deck of cards, and implement a shuffle() method, 
   and a draw(n) method (where you draw n cards). Calling draw() when the deck is empty returns an empty array.

const deck = new Deck();
deck.shuffle();
console.log(deck.draw(5)); // Example: ['10♠', 'K♥', '3♣', 'J♦', '7♠']
console.log(deck.draw(5).length); // 5
console.log(deck.draw(2)); // Example: ['5♣', 'A♠']
"""

class Deck:
    import random

    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [f"{rank}{suit}" for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        self.random.shuffle(self.cards)

    def draw(self, n):
        drawn_cards = self.cards[:n]
        self.cards = self.cards[n:]
        return drawn_cards
    
if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    print(deck.draw(5))  # Example: ['10♠', 'K♥', '3♣', 'J♦', '7♠']
    print(len(deck.draw(5)))  # 5
    print(deck.draw(2))  # Example: ['5♣', 'A♠']

