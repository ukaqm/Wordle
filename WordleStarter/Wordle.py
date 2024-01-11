# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    #CHECKS if entered string is a valid word.
    def enter_action(entered_word):
        # Convert the entered word to uppercase for comparison
        entered_word = entered_word.lower()

        # Check if the entered word is valid (in the list of words)
        if entered_word not in FIVE_LETTER_WORDS:
            gw.show_message("Invalid word. Try again.")
            return
        else:
            gw.show_message("This is a valid word.")
        
        

    #RANDOMLY CHOOSES the word for user to guess
    word = random.choice(FIVE_LETTER_WORDS)
    print(word)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    #PRINTS word onto first row of wordle grid completing milestone 1 task
    for iCount in range(N_ROWS):
        gw.set_square_letter(0, iCount, word[iCount])

# Startup code

if __name__ == "__main__":
    wordle()

