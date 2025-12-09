#!/usr/bin/env python3
from cards import *

deck = Deck()
deck.shuffle()

for _ in range(100):
    hand = deck.draw(5)
    print("Drew hand:", hand, end=' ')
    print(f"({len(deck.cards)} cards left in deck)")
    if len(deck.cards) < 5:
        print("Not enough cards left, reshuffling the deck.")
        deck = Deck()
        deck.shuffle()


