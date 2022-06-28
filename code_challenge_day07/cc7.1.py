"""
---------------------------------------------------------------------------
Day07: Hangman Game[Beginner]
Code Challenge 7.1: Picking a Random Words and Checking Answers
Final Code Preview: https://repl.it/@appbrewery/Day-7-Hangman-1-End
Things to learn:
    - Iteration: for-in loop
    - Collection: list
    - Conditionals: if-else
    - Module: random module
    - Random method: shuffle()
*** Press 'Run' button to understand how does the challenge work
---------------------------------------------------------------------------
"""

import random

print('Picking a Random Words and Checking Answers:')

word_list = ["python", "jumble", "easy", "difficult", "answer"]
random.shuffle(word_list)
guess_letter = input('Pick a letter & check whether that letter is in the word or not!\n')

for letter in word_list[0]:
    if letter == guess_letter:
        print('right')
    else:
        print('Wrong')
