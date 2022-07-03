"""
-------------------------------------------------------------------------
Day12: Scope & Number Guessing Game
Project12: The Number Guessing Game
Code Overview: Go through the TODO
Code Preview: https://replit.com/@appbrewery/guess-the-number-final?embed=1&output=1#art.py
*** Press 'Run'/ 'play' button to understand how does the challenge work
--------------------------------------------------------------------------
TODO-01: Include an ASCII art logo.
TODO-02: Allow the player to submit a guess for a number between 1 and 100.
TODO-03: Check user's guess against actual answer. Print "Too high."
    or "Too low." depending on the user's answer.
TODO-04: If they got the answer correct, show the actual answer to the player.
TODO-05: Track the number of turns remaining.
TODO-06: If they run out of turns, provide feedback to the player.
TODO-07: Include two different difficulty levels
    e.g., 10 guesses in easy mode, only 5 guesses in hard mode

"""
import random
import art

print(art.logo)
rand_num = random.randint(1, 100)
game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def predicted_number(random_number, guessed_number):
    if guessed_number < random_number:
        print('Too low.')
    elif guessed_number > random_number:
        print('Too high.')
    elif guessed_number == random_number:
        print(f'You got it! The answer was {random_number}')
        return 'q'


def set_difficulty(level):
    if level == 'easy':
        count_guess = 10
        return count_guess
    elif level == 'hard':
        count_guess = 5
        return count_guess


number_of_attempts = set_difficulty(game_difficulty)
for x in range(0, number_of_attempts):
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    guess = int(input('Make a guess: '))
    if predicted_number(rand_num, guess) == 'q':
        break
    number_of_attempts = number_of_attempts - 1

    if number_of_attempts == 0:
        print(f"Sorry mate! you've lost. The correct answer was {rand_num}")

    print('Guess again.')

"""
------------------------------------------------------------------------------
Things you'll learn:
    - User defined function: 
        - predicted_number(random_number, guessed_number)
        - set_difficulty(level)
    - Conditional: if-else
    - Iteration: for-in, range(), break    
    - Module: art(user defined)
---------------------------------------------------------------------------------  
"""
