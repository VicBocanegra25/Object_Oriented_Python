"""
An implementation of a card game using Procedural Programming.
The purpose of the game is to guess if the next card drawn from a deck will be higher or lower than the current one
@author: Víctor Bocanegra
@date: 07/04/2023

Example based on the book OOP from Irv Kalb
"""

import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

# We'll play the game N number of times
NCARDS = 8


def get_card(deck_list_in):
    """
    The get_card() function passes in a deck and it returns a random card from the deck.
    @params:
        deck_list_in -> list []: A list of card dictionaries representing the deck
    @returns:
        this_card -> dict {}: A dictionary representing the drawn card with keys: 'rank', 'suit' and 'value'.
    """
    this_card = deck_list_in.pop()
    return this_card


def shuffle(deck_list_in):
    """
    The shuffle() function returns a shuffled copy of the deck
    @params:
        deck_list_in -> list[]: A list of card dictionaries representing the deck
    @returns:
        deck_list_out -> list[]: A list of card dictionaries representing a shuffled deck
    """
    deck_list_out = deck_list_in.copy()
    random.shuffle(deck_list_out)
    return deck_list_out


def play_game(starting_deck_list, score):
    """
    The play_game() function plays the card game a single time.

    @params:
        game_deck_list -> list[]: list of card dictionaries representing the shuffled deck
        score -> int: An integer representing the initial score
        NCARDS -> int: An integer representing the number of cards to play in the game
    @returns:
        final_score -> int: An integer representing the final score after playing the game
    """
    # A variable storing a dict of the current card
    game_deck_list = shuffle(starting_deck_list)
    current_card_dict = get_card(game_deck_list)
    # Getting the rank, value and suit of the current card
    current_card_rank = current_card_dict['rank']
    current_card_suit = current_card_dict['suit']
    current_card_value = current_card_dict['value']

    print(f"Starting card is {current_card_rank} of {current_card_suit}.\n")

    # The user will guess NCARD times
    for card in range(0, NCARDS):

        # Checking for the user's response, must be either an l or an h
        while True:
            answer = input(f"Will the next card be higher or lower than the {current_card_rank} of {current_card_suit}? (Enter h or l): ")
            answer = answer.casefold() # Force lower case

            if answer != 'h' and answer != 'l':
                print("Invalid answer, please try again.\n")
                answer = input(f"Will the next card be higher or lower than the {current_card_rank} of {current_card_suit}? (Enter h or l): ")
            else:
                break

        # To continue the game, we make the user guess the next card
        next_card_dict = get_card(game_deck_list)
        # Getting the rank, suit and value
        next_card_rank = next_card_dict['rank']
        next_card_suit = next_card_dict['suit']
        next_card_value = next_card_dict['value']

        print(f"Next card is {next_card_rank} of {next_card_suit}.\n")

        # Evaluating the user's answer and scoring
        if answer == 'h':
            if next_card_value > current_card_value:
                print("You got it right. It was higher!")
                score += 20
            else:
                print("Sorry, you got it wrong.")
                score -= 15

        elif answer == 'l':
            if next_card_value < current_card_value:
                print("You got it right. It was lower!")
                score += 20
            else:
                print("Sorry, you got it wrong.")
                score -= 15

        print(f"Your score is: {score}.\n")
        current_card_rank = next_card_rank
        current_card_value = next_card_value
        current_card_suit = next_card_suit
    return score


def main():
    """
    The main() function uses a while loop to run the game as long as the player wants to.
    We start with an initial score of 50.
    """
    print('Welcome to Higher or Lower.')
    print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
    print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
    print('You have 50 points to start.\n')

    # Building the deck to play
    starting_deck_list = []
    for suit in SUIT_TUPLE:
        for value, rank in enumerate(RANK_TUPLE):
            card_dict = {'rank': rank, 'suit': suit, 'value': value + 1}
            starting_deck_list.append(card_dict)

    score = 50

    while True:  # play multiple games
        score = play_game(starting_deck_list, score)

        # Checking if the user wants to continue playing
        go_again = input('To play again, press ENTER, or "q" to quit: ')
        if go_again == 'q':
            break

    print(f'OK bye. Your final score was: {score}')


if __name__ == '__main__':
    main()
