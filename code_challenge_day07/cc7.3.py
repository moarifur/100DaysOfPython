"""
--------------------------------------------------------------------------------------------
Day07: Hangman Game[Beginner]
Code Challenge 7.3: Checking if the Player has Won
Final Code Preview: https://replit.com/@appbrewery/Day-7-Hangman-3-End
Things to learn:
    - Iteration: for-in loop
    - Collection: list, string
    - List Method: append(), count() - https://www.w3schools.com/python/ref_list_count.asp
    - String Method: count() - https://www.w3schools.com/python/ref_string_count.asp
    - Conditionals: if-else
    - Module: random module
    - Random method: choice()
*** Press 'Run' button to understand how does the challenge work
-----------------------------------------------------------------------------------------------
"""

import random

print('Picking a Random Words and Checking Answers:\n')
word_list = ["python", "jumble", "easy", "difficult", "answer"]
chosen_word = random.choice(word_list)
display = []

# Cheat
print(f'Your answer will be: {chosen_word}')

# Creating blanks
for x in chosen_word:
    display.append('_')

# Filling the blank with guessing word if that matches with the chosen_word
while True:
    guess_letter = input('Pick a letter & check whether that letter is in the word or not!\n').lower()

    for letter in chosen_word:
        if letter == guess_letter:
            display[chosen_word.index(letter)] = letter

    if display.count('_') == 0:
        break

    print(display)
