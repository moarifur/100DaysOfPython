"""
---------------------------------------------------------------------------
Day07: Hangman Game[Beginner]
Code Challenge 7.2: Replacing Blanks with Guesses
Final Code Preview: https://replit.com/@appbrewery/Day-7-Hangman-2-End
Things to learn:
    - Iteration: for-in loop
    - Collection: list
    - List Method: append()
    - Conditionals: if-else
    - Module: random module
    - Random method: choice()
*** Press 'Run' button to understand how does the challenge work
---------------------------------------------------------------------------
"""

import random

print('Picking a Random Words and Checking Answers:\n')
word_list = ["python", "jumble", "easy", "difficult", "answer"]
chosen_word = random.choice(word_list)
guess_letter = input('Pick a letter & check whether that letter is in the word or not!\n').lower()
display = []


# Creating blanks
for x in chosen_word:
    display.append('_')

# Filling the blank with guessing word if that matches with the chosen_word
for letter in chosen_word:
    if letter == guess_letter:
        display[chosen_word.index(letter)] = letter
        # print(chosen_word.index(letter))

print(display)
