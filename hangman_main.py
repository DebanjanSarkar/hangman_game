import os

import hangman_ascii_art as asc
import fetch_word as fw
import utility as util

asc.display_hangman_title()

input("Press Enter to Play!")

# Setting a single word in the word space while debugging
# actual_word = "beekeeper"

# Getting a random word from the list of words in the glossary.
actual_word = fw.get_a_random_word()

# This is the variable that will contain the letters in correct places, when any letter is correctly guessed.
# One underscore '_' denotes one blank space at which letter occurs, and one space ' ' after it for better readability to user.
guess_word = '_ ' * len(actual_word)


print("""
You need to get the word by guessing it letter by letter, before hangman completely loses its life. 
For each wrong guess, you lose a Life, and hangman proceeds one step towards death.
As a starting hint, it contains following number of alphabets.
      """)

stage = 0
letters_already_entered = set()
while stage < asc.get_max_stage():
    # Shows how many blank spaces are still left to be guessed.
    print("\n",guess_word, end="\n\n")

    # Displays the current stage of hangman, so that user gets to know how many more chances is left!
    asc.display_hangman_stage(stage)
    # Displays the letters that has already been entered by user
    if len(letters_already_entered) > 0:
        print("Letters already entered: ", letters_already_entered)
    
    #------------------------------------------------------------------------------------------------------
    # Prompts the user to enter an Alphabet (conversion to upper case makes user input not case-sensitive)
    letter = input("Guess a letter (Enter dot '.' for a single letter HINT): ").upper()[0]
    #------------------------------------------------------------------------------------------------------

    # Clear the screen for better user's experience
    os.system('cls')


    if letter == ".":
        if guess_word.count("_") > 1:
            # Hint will be given only if user enters "." and there are more than 1 blank space.
            guess_word = util.hint(actual_word, guess_word)
            continue
        elif guess_word.count("_") == 1:
            print("\n\nCannot display hint as only 1 letter is left to be guessed.")
            continue

    # Adding the recently input alphabet to the 'letters_already_entered' set
    letters_already_entered.add(letter)

    if letter not in actual_word:
        # Guessed letter does not exists in the word.
        print(f"You guessed '{letter}', that's not in the word. You lose a life.")
        stage += 1
    else:
        # Guessed letter exists single or multiple times in the word.
        print("Correctly guessed! Go On!!!")
        guess_word = util.fill_matching_letters_in_blank_spaces(actual_word, guess_word, letter)
    
    # Check condition to see whether the word is completely guessed.
    if '_' not in guess_word:
        print("\n\n",guess_word)
        print("You guessed the word correctly! YOU WIN!!!")
        asc.display_win()
        break
else:
    # Hangman max stage reached.
    print(f"\n\nThe correct word is: {actual_word}\n\n")
    asc.display_hangman_stage(stage)
    print("Hangman was completely put to death! YOU LOSE!")
    asc.display_lose()

input("Press Enter to Exit!")

    
    