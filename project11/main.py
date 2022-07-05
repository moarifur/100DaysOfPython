"""
-------------------------------------------------------------------------
Day11: The Blackjack Capstone Project
Project11: Blackjack
Code Overview: Go through the TODO or Rule
Code Preview: https://replit.com/@appbrewery/blackjack-final
*** Press 'Run'/ 'play' button to understand how does the challenge work
https://www.jetbrains.com/help/pycharm/part-1-debugging-python-code.html#hex-format
--------------------------------------------------------------------------
TODO-01(Rule-01): The deck is unlimited in size.
TODO-02(Rule-02): The Jack/Queen/King all count as 10.
TODO-03(Rule-03): The the Ace can count as 11 or 1.
TODO-04(Rule-04): The cards in the list have equal probability of being drawn.
TODO-05(Rule-05): Cards are not removed from the deck as they are drawn.
TODO-06(Rule-06): The computer is the dealer.
TODO-07(Rule-07): Use the following list as the deck of cards:
                    - cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                    - There are no jokers.
"""
import os
import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
computer = []


def preset():
    os.system('cls')
    print(logo)


# TODO-07
def player_shuffle_cards():
    random.shuffle(cards)
    player.append(cards[0])
    return player


def computer_shuffle_cards():
    random.shuffle(cards)
    computer.append(cards[0])
    return computer


def shuffle_cards():
    player_shuffle_cards()
    computer_shuffle_cards()


def player_score():
    if 11 in player and sum(player) > 21:
        if player[0] != 11:
            player.remove(11)
            player.append(1)
    score = sum(player)
    return score


def computer_score():
    if 11 in computer and sum(computer) > 21:
        if computer[0] != 11:
            computer.remove(11)
            computer.append(1)
    score = sum(computer)
    return score


def check_player_rules():
    while player_score() < 31:
        if player_score() == 21:
            print(f"Your final hands: {player}, final score: {player_score()}")
            print("It's a blackjack! You win 😎")
            break
        elif player_score() > 21:
            print(f"Your final hands: {player}, final score: {player_score()}")
            print(f"Computer's final hands: {computer}, final score: {computer_score()}")
            print("It's a bust! You Lose 😤")
            break
        elif player_score() == computer_score():
            print(f"Your final hands: {player}, final score: {player_score()}")
            print(f"Computer's final hands: {computer}, final score: {computer_score()}")
            print("It's draw! 😤")
            break
        else:
            break


def check_computer_rules():
    while computer_score() < 31:
        if computer_score() == 21:
            print(f"Computer's final hands: {computer}, final score: {computer_score()}")
            print("It's a blackjack! Computer win 😎")
            break
        elif computer_score() > 21:
            print(f"Your final hands: {player}, final score: {player_score()}")
            print(f"Computer's final hands: {computer}, final score: {computer_score()}")
            print("It's a bust! Computer Lose 😤. So you win 😎")
            break
        elif player_score() == computer_score():
            print(f"Your final hands: {player}, final score: {player_score()}")
            print(f"Computer's final hands: {computer}, final score: {computer_score()}")
            print("It's draw! 😤")
            break
        elif player_score() < computer_score() <= 20:
            print(f"Your final hands: {player}, final score: {player_score()}")
            print(f"Computer's final hands: {computer}, final score: {computer_score()}")
            print("Computer wins 😎! So You Lose 😤")
            break
        computer_shuffle_cards()


flag = 0
shuffle_cards()
shuffle_cards()
choose = input("Do you wanna play a game of Blackjack? Type 'y' to play or 'n' to pass: ")
if choose == 'y':
    preset()
    while True:
        if flag == 0:
            print(f"Your cards: {player}, current score: {player_score()}")
            print(f"Computer's first cards {computer[0]}")
            flag = 1

        if player_score() == 21 and len(player) == 2:
            print("It's a blackjack! You win 😎")
        else:
            play_game = input("Type 'y' to get another card, type 'n' to pass: ")
            if play_game == 'y':
                shuffle_cards()
                check_player_rules()
            elif play_game == 'n':
                check_computer_rules()

elif choose == 'n':
    print("Why bother!!")

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

#         if player_score == 21:
#             print("It's a blackjack! You win!!")
#             break
#         elif player_score > 21:
#             print("It's a bust! You lose.")
#             break
#         elif player_score < 21:
#             print("You can hit!!")

#         if computer_score == 21:
#             print("It's a blackjack! Computer win!!")
#             break
#         elif computer_score > 21:
#             print("It's a bust! You lose.")
#             break
#         elif computer_score < 21:
#             print("You can hit!!")


# def play_game():
#     if flag == 0:
#         input("Type 'y' to get another card, type 'n' to pass: ")
#         print(f"Your cards: {player}, current score: {player_score()}")
#         print(f"Computer's first cards {computer[0]}")
#     elif flag == 1:
#         print(f"Your cards: {player}, current score: {player_score()}")
#         print(f"Computer's cards: {computer}, current score: {computer_score()}")
#     return flag
