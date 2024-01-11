# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS

#Imported colors for the correct, present, and missing letters
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():

    def enter_action(entered_word):

        #Convert the entered word to uppercase for comparison
        entered_word = entered_word.upper()

        #Check if the entered word is valid (in the list of words)
        if entered_word not in map(str.upper, FIVE_LETTER_WORDS):
            gw.show_message("Invalid word. Try again.")
            return
        else:
            print('Valid Word')
            current_row = gw.get_current_row()

            if gw.get_current_row() < N_ROWS:
                word_remaining = list(word)

                #First pass: Mark correct letters and remove them from word_remaining
                for iCount in range(N_COLS):
                    gw.set_square_letter(current_row, iCount, entered_word[iCount])
                    if entered_word[iCount] == word[iCount]:
                        gw.set_square_color(current_row, iCount, CORRECT_COLOR)
                        #Removes letter from consideration as it is known that it is part of the word and in the correct position
                        word_remaining[iCount] = None  

                #Second pass: Check for present letters
                for iCount in range(N_COLS):
                    if entered_word[iCount] != word[iCount] and entered_word[iCount] in word_remaining:
                        gw.set_square_color(current_row, iCount, PRESENT_COLOR)
                        #Removes letter from consideration as it is known that it is part of the word BUT NOT in the correct position
                        word_remaining[word_remaining.index(entered_word[iCount])] = None  
                    #If letter isn't present color is gray.
                    elif gw.get_square_color(current_row, iCount) != CORRECT_COLOR:
                        gw.set_square_color(current_row, iCount, MISSING_COLOR)

                
                # Check if the word matches the target word
                if entered_word == word.upper():
                    gw.show_message("Congratulations! You've guessed the word.")
                    return

                # Move to the next row
                if current_row == N_ROWS - 1:
                    gw.show_message("Game over! The word was " + word)
                    return
                else:
                    gw.set_current_row(current_row + 1)
        

    #Randomly chooses the word for user to guess
    word = random.choice(FIVE_LETTER_WORDS).upper()
    print(word)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    #Sets current row to the first row
    gw.set_current_row(0)

# Startup code

if __name__ == "__main__":
    wordle()

