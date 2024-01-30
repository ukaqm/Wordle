# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from WordleDictionary import FIVE_LETTER_WORDS

#Imported colors for the correct, present, and missing letters
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, CB_CORRECT_COLOR, CB_PRESENT_COLOR

def wordle():
    gw = WordleGWindow()
    gw.create_colorblindmode_button()
    gw.create_hardmode_button()
    gw.create_newgame_button()
    word = gw.new_word()
    print(word)

    def enter_action(entered_word):
        if gw.hard_mode:
            is_valid, message = gw.hard_mode_constraints(entered_word)
            if not is_valid:
                gw.show_message(message)
                return
        #Convert the entered word to uppercase for comparison
        entered_word = entered_word.upper().strip()
        correct_color = CB_CORRECT_COLOR if gw.colorblind_mode else CORRECT_COLOR
        present_color = CB_PRESENT_COLOR if gw.colorblind_mode else PRESENT_COLOR

        if len(entered_word) != 5:
            print("Word length check triggered")  # Debugging print statement
            gw.show_message("Word must have 5 letters. Try again.")
            return
        #Check if the entered word is valid (in the list of words)
        elif entered_word not in map(str.upper, FIVE_LETTER_WORDS):
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
                        gw.set_square_color(current_row, iCount, correct_color)
                        # Set key color to CORRECT_COLOR if it's not already set
                        if gw.get_key_color(letter) != correct_color:
                            gw.set_key_color(letter, correct_color)
                        word_remaining[iCount] = None





                for iCount in range(N_COLS):
                        letter = entered_word[iCount].upper()

                        if letter == word[iCount]:
                            # Update correct_letters for hard mode
                            gw.correct_letters[iCount] = letter
                            # ... rest of the code for coloring the square ...

                        elif letter in word_remaining:
                            # Update present_letters for hard mode
                            gw.present_letters.add(letter)
                            # ... rest of the code for coloring the square ...

                        else:
                            # Update absent_letters for hard mode
                            gw.absent_letters.add(letter)
                            # ... rest of the code for coloring the square ...





                        

                for iCount in range(N_COLS):
                    letter = entered_word[iCount].upper()  # Get the uppercase letter

                    # Second pass: Check for present letters
                    if letter != word[iCount] and letter in word_remaining:
                        gw.set_square_color(current_row, iCount, present_color)
                        # Set key color to PRESENT_COLOR if it's not already set to CORRECT_COLOR
                        if gw.get_key_color(letter) not in [correct_color, present_color]:
                            gw.set_key_color(letter, present_color)
                        word_remaining[word_remaining.index(letter)] = None
                    elif gw.get_square_color(current_row, iCount) != correct_color:
                        gw.set_square_color(current_row, iCount, MISSING_COLOR)
                        # Set key color to MISSING_COLOR if it's not already set to CORRECT_COLOR or PRESENT_COLOR
                        if gw.get_key_color(letter) not in [correct_color, present_color]:
                            gw.set_key_color(letter, MISSING_COLOR)














                            
                    
                # Check if the word matches the target word
                if entered_word == word.upper():
                    if (current_row + 1) == 1:
                        gw.show_message("Congrats! You got the word on your first try!")
                    else:
                        gw.show_message("Congrats! You got the word in " + str(current_row + 1) + " attempts")
                        return

                # Move to the next row
                if current_row == N_ROWS - 1:
                    gw.show_message("Game over! The word was \"" + word +"\"")
                    return
                else:
                    gw.set_current_row(current_row + 1)
        
    #Randomly chooses the word for user to guess

    gw.add_enter_listener(enter_action)
    #Sets current row to the first row
    gw.set_current_row(0)

# Startup code

if __name__ == "__main__":
    wordle()