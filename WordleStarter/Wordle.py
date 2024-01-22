# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""
# ignore this comment
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
            current_row = gw.get_current_row()
            print('Valid Word\n' + 'Number of attempts: ' + str(current_row + 1))

            if gw.get_current_row() < N_ROWS:
                word_remaining = list(word)

                for iCount in range(N_COLS):
                    letter = entered_word[iCount].upper()  # Get the uppercase letter
                
                # First pass: Mark correct letters and remove them from word_remaining
                    if letter == word[iCount]:
                        gw.set_square_color(current_row, iCount, CORRECT_COLOR)
                        # Set key color to CORRECT_COLOR if it's not already set
                        if gw.get_key_color(letter) != CORRECT_COLOR:
                            gw.set_key_color(letter, CORRECT_COLOR)
                        word_remaining[iCount] = None

                for iCount in range(N_COLS):
                    letter = entered_word[iCount].upper()  # Get the uppercase letter

                    # Second pass: Check for present letters
                    if letter != word[iCount] and letter in word_remaining:
                        gw.set_square_color(current_row, iCount, PRESENT_COLOR)
                        # Set key color to PRESENT_COLOR if it's not already set to CORRECT_COLOR
                        if gw.get_key_color(letter) not in [CORRECT_COLOR, PRESENT_COLOR]:
                            gw.set_key_color(letter, PRESENT_COLOR)
                        word_remaining[word_remaining.index(letter)] = None
                    elif gw.get_square_color(current_row, iCount) != CORRECT_COLOR:
                        gw.set_square_color(current_row, iCount, MISSING_COLOR)
                        # Set key color to MISSING_COLOR if it's not already set to CORRECT_COLOR or PRESENT_COLOR
                        if gw.get_key_color(letter) not in [CORRECT_COLOR, PRESENT_COLOR]:
                            gw.set_key_color(letter, MISSING_COLOR)
                    
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

