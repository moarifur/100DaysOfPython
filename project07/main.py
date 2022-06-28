"""
--------------------------------------------------------------------------------------------
Day07: Hangman Game[Beginner]
Project07: Hangman - A guessing game
Final Code Preview: https://replit.com/@appbrewery/Day-7-Hangman-5-End
Things to learn:
    - Iteration: for-in loop
    - Collection: list, string
    - List Method: append(), count() - https://www.w3schools.com/python/ref_list_count.asp
    - String Method: count() - https://www.w3schools.com/python/ref_string_count.asp
    - Conditionals: if-else
    - Module: random module
    - Use of 'from' keyword:
        - create user defined module(.py file)
        - import variable / function from other module
    - Random method: choice()
    - ASCII Art
*** Press 'Run'/ 'play' button to understand how does the challenge work
-----------------------------------------------------------------------------------------------
"""

import random
from hangman_wordlist import word_list
from hangman_art import logo
from hangman_art import stages

chosen_word = random.choice(word_list)
display = []
life = 6

# print logo
print(logo)
# Cheat
print(f'Your answer will be: {chosen_word}')

# Creating blanks
for x in chosen_word:
    display.append('_')

# Create an infinite loop
while True:
    guess_letter = input('Pick a letter & check whether that letter is in the word or not!\n').lower()

    # Filling the blank with guessing word
    if guess_letter in chosen_word:
        # Filling all duplicate letters
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess_letter:
                display[position] = chosen_word[position]
        # Show word list in progress
        print(display)
        # What the hangman's current position
        print(stages[life])
    else:
        print(display)
        life -= 1
        print(stages[life])

    if life == 0:
        print('You Lose!!')
        break
    elif display.count('_') == 0:
        print('You Win!')
        break


