"""
--------------------------------------------------------------------------------------------
Day07: Hangman Game[Beginner]
Code Challenge 7.4: Keeping Track of the Player's Lives
Final Code Preview: https://replit.com/@appbrewery/Day-7-Hangman-4-End
Things to learn:
    - Iteration: for-in loop
    - Collection: list, string
    - List Method: append(), count() - https://www.w3schools.com/python/ref_list_count.asp
    - String Method: count() - https://www.w3schools.com/python/ref_string_count.asp
    - Conditionals: if-else
    - Module: random module
    - Random method: choice()
    - ASCII Art
*** Press 'Run'/ 'play' button to understand how does the challenge work
-----------------------------------------------------------------------------------------------
"""

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["python", "jumble", "easy", "difficult", "answer"]
chosen_word = random.choice(word_list)
display = []
life = 6

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


