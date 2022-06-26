"""
---------------------- Alternative way ------------------------------------
Day04: Randomisation and Python Lists[Beginner]
Project04: Rock, Paper & Scissors Game
Description: Flowchart in project04.png
Steps:
    - Variable, input function, type casting
    - conditionals: if, elif and else
    - Random Module: randint(start, end)
    - list
    - ASCII Art Archive: https://www.asciiart.eu/
    [https://www.asciiart.eu/people/body-parts/hand-gestures]
---------------------------------------------------------------------------
"""
import random

print('Welcome to Rock, Paper & Scissors Game.')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for 'Rock', 1 for 'Paper', 2 for 'Scissors':\n"))
print(f"User's Choice: {game_image[user]}")
computer = random.randint(0, 2)
print(f"Computer's Choice: {game_image[computer]}")

if user >= 3 or user < 0:
    print("You typed an invalid number, you lose!")
elif user == computer:
    print("It's a draw!!")
elif user == 2 and computer == 0:
    print('You Lose! 😞')
elif user == 0 and computer == 2:
    print('You Win! 😊')
elif user < computer:
    print('You Lose! 😞')
elif user > computer:
    print('You Win! 😊')


# """
# ---------------------------------------------------------------------------
# Day04: Randomisation and Python Lists[Beginner]
# Project04: Rock, Paper & Scissors Game
# Description: Flowchart in project04.png
# Steps:
#     - Variable, input function, type casting
#     - conditionals: if, elif and else
#     - Random Module: randint(start, end)
#     - list
# ---------------------------------------------------------------------------
# """
# import random
#
# print('Welcome to Rock, Paper & Scissors Game.')
# user = int(input("What do you choose? Type 0 for 'Rock', 1 for 'Paper', 2 for 'Scissors': "))
# computer = random.randint(0, 2)
# print(f"Computer's Choice: {computer}")
# choice = ['Rock', 'Paper', 'Scissors']
#
# if user == computer:
#     print('Tie')
# elif choice[user] == 'Rock' and choice[computer] == 'Paper':
#     print('You Lose! 😞')
# elif choice[user] == 'Rock' and choice[computer] == 'Scissors':
#     print('You Win! 😊')
# elif choice[user] == 'Paper' and choice[computer] == 'Scissors':
#     print('You Lose! 😞')
# elif choice[user] == 'Paper' and choice[computer] == 'Rock':
#     print('You Win! 😊')
# elif choice[user] == 'Scissors' and choice[computer] == 'Rock':
#     print('You Lose! 😞')
# elif choice[user] == 'Scissors' and choice[computer] == 'Paper':
#     print('You Win! 😊')


