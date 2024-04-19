# Mexe-mexe

This is a program I developed specifically for Mexe-mexe, a card game I play with my grandparents. The point of the program is simple: given a current state of the game, determine if a given card can fit with the others already on the table, following specific rules of the game. I initially developed it with a GUI, but I don't update it anymore. The CLI version is way better to use on a phone. I would not recommend using it as it is.

# Rules of the Game

Mexe-mexe is a puzzle card game. Each player starts with 11 cards, and the goal is to "exit" the game by not having any cards left on your hand. To do so, players take turns, and at each turn you choose between 3 options: putting 3 cards on the table, putting 1 card on the table, or drawing a card. To put cards on the table, one must make sure that, after adding their cards, the cards on the table are either numbered sequences (A 1 2 3 4 5 6 7 8 9 10 J Q K A) of 3 or more cards that have the same suit, or cards that have that have the same number, but different suits (3 or 4 cards, 3 being the minimum, 4 being the maximum since there are only 4 different suits). The game ends when only one player is left with cards on their hand.

# Compilation

Dependency (for the GUI): `tkinter 8.6`
Simply run:
`python mexe-mexeCLI.py` or `python mexe-mexeGUI.py

# CLI Usage
To use the CLI version, you can type `add`, `verify`, `verify -s` or `reset`. When you type `add`, it will prompt you to enter a card to add it to the table. You can enter cards in different formats. The obvious one is to add an individual card. To do this, one must simply type the number of the card followed by its suit, for example: `4C`. You can also add a sequence of 3 or more cards of the same suit, for example `(A 2 3 4)C` adds AC, 2C, 3C and 4C to the table. The last possibility is adding cards with the same number, but different suits. To do this, one must type the number of the card followed by 3 or more suits. For example: `4CPE` adds 4C, 4P and 4E to the table. Any character can be used to distinguish the suits, as long as you are consistent (use 4 different characters for the 4 different suits).

The `verify` command is the main command in this program. When you type `verify`, it will prompt you to enter a card (in the single card format). When you do so, it will tell you if the card can be added to the table while maintaining a valid combination. If you type `verify -s`, it will again prompt you to enter a card, but now it will show you a valid way of organizing the cards on the table with your card in it.

The `reset` command clears the table.
