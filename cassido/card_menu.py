#!/usr/bin/env python3
"""Interactive menu to draw a hand or reshuffle the deck."""
from cards import Deck
import sys


def get_single_key():
    """Read a single keypress from stdin without requiring Enter.

    Works on Unix (macOS/Linux) using `termios`/`tty`, and falls back to
    `msvcrt` on Windows.
    """
    try:
        import termios, tty
    except Exception:
        # Windows
        try:
            import msvcrt
            ch = msvcrt.getch()
            if isinstance(ch, bytes):
                return ch.decode('utf-8', errors='ignore')
            return ch
        except Exception:
            # Last resort: normal input (requires Enter)
            return sys.stdin.read(1)

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def prompt_int(prompt, default=None):
    try:
        val = input(prompt).strip()
        if val == "" and default is not None:
            return default
        return int(val)
    except (ValueError, TypeError):
        return None


def main():
    deck = Deck()
    deck.shuffle()

    menu = (
        "\nCard Menu:\n"
        "1) Draw hand\n"
        "2) Reshuffle (reset deck)\n"
        "3) Show remaining count\n"
        "4) Show remaining cards\n"
        "5) Exit\n"
    )

    while True:
        print(type(menu))
        print(menu)
        print("Press a single key 1-5 to choose an option:", end=" ", flush=True)
        choice = get_single_key()
        # echo the pressed key and newline for clarity
        print(choice)
        if choice is None:
            print("No input detected.")
            continue
        choice = choice.strip()
        if choice == "1":
            n = prompt_int("How many cards to draw (default 5): ", default=5)
            if n is None or n < 0:
                print("Please enter a valid non-negative integer.")
                continue
            hand = deck.draw(n)
            if not hand:
                print("No cards left to draw.")
            else:
                print("You drew:", hand)
                print(f"{len(hand)} card(s) drawn; {len(deck.cards)} remaining.")
        elif choice == "2":
            deck = Deck()
            deck.shuffle()
            print("Deck reshuffled (reset to full 52 cards).")
        elif choice == "3":
            print(f"{len(deck.cards)} card(s) remaining in the deck.")
        elif choice == "4":
            print(deck.cards)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Unknown option. Please choose 1-5.")


if __name__ == "__main__":
    main()
