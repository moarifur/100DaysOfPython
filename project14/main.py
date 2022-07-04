"""
-------------------------------------------------------------------------
Day14: Higher Lower Game Project
Project14: Higher Lower Game Project
Code Overview: Go through the TODO
Code Preview: https://replit.com/@appbrewery/higher-lower-final
*** Press 'Run'/ 'play' button to understand how does the challenge work
--------------------------------------------------------------------------
TODO-01: Generate a random account from the game data.
TODO-02: Format account data into printable format.
TODO-03: Ask user for a guess.
TODO-04: Check if user is correct, get follower count & feedback.
TODO-05: If user is wrong, end the game & feedback.
TODO-06: Make B become the next A.
TODO-07: Add art & Clear screen between rounds.

"""

import os
import random
import time
import art
import game_data

print(art.logo)


def preset():
    os.system('cls')
    print(art.logo)


def data_executor(first_rand, second_rand):
    name_a = game_data.data[first_rand]['name']
    description_a = game_data.data[first_rand]['description']
    country_a = game_data.data[first_rand]['country']
    follower_count_a = game_data.data[first_rand]['follower_count']
    # choose_a = f"{name_a}, {description_a}, from {country_a} - {follower_count_a}"
    choose_a = f"{name_a}, {description_a}, from {country_a}"

    name_b = game_data.data[second_rand]['name']
    description_b = game_data.data[second_rand]['description']
    country_b = game_data.data[second_rand]['country']
    follower_count_b = game_data.data[second_rand]['follower_count']
    # choose_b = f"{name_b}, {description_b}, from {country_b} - {follower_count_b}"
    choose_b = f"{name_b}, {description_b}, from {country_b}"

    if follower_count_a > follower_count_b:
        return 'a', choose_a, choose_b
    else:
        return 'b', choose_a, choose_b


score = 0
f_rand = random.randint(0, 49)
while True:
    s_rand = random.randint(0, 49)
    data = data_executor(f_rand, s_rand)
    # print(data)
    # print(type(data))
    # print(data[0])

    print(f'Compare A: {data[1]}')
    print(art.vs)
    print(f'Against B: {data[2]}')

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    preset()
    if guess == data[0]:
        score += 1
        print(f"You're right! Current score: {score}.")
        f_rand = s_rand
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        time.sleep(3.5)
        break

"""
------------------------------------------------------------------------------
Things you'll learn:
    - User defined function: 
        - data_executor(first_rand, second_rand)
        - preset()
    - Conditional: if-else
    - Iteration: while, break    
    - Module: art(user defined)
    - Function multiple return - tuples
    - Tuples - access tuples
---------------------------------------------------------------------------------  
"""
