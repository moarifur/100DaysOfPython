"""
---------------------------------------------------------------------------
Day03: Control Flow and Logical Operators[Beginner]
Project03: Treasure Island
Description: Flowchart in project03.jpg
Steps:
    - Variable, input function
    - conditionals: if, elif and else
    - python string method
---------------------------------------------------------------------------
"""

print('Welcome to Treasure Island. Your mission is to find the treasure.')

direction = input("You're at a cross road. Where do you wanna go? Type 'left' or 'right'?\n").lower()
if direction == 'left':
    action = input("You've come to a lake. There is an island in the middle of the lake. "
                   "Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
    if action == 'wait':
        door = input("You arrive at the island unharmed. "
                     "There is a house with 3 doors. One red, one yellow and one blue. "
                     "Which colour do you choose?\n").lower()
        if door == 'yellow':
            print('You Win!')
        elif door == 'red':
            print('Burned by fire. Game Over.')
        elif door == 'blue':
            print('Eaten by beasts. Game Over.')
        else:
            print('Game Over.')
    else:
        print('Attacked by trout. Game Over.')
else:
    print('Fall into a hole. Game Over.')


# if direction == 'right' or '':
#     print('Fall into a hole. Game Over.')
# elif direction == 'left' or action == 'swim' or '':
#     print('Attacked by trout. Game Over.')
# elif direction == 'left' or action == 'wait' or door == 'red':
#     print('Burned by fire. Game Over.')
# elif direction == 'left' or action == 'wait' or door == 'blue':
#     print('Eaten by beasts. Game Over.')
# elif direction == 'left' or action == 'wait' or door == '':
#     print('Game Over.')
# elif direction == 'left' or action == 'wait' or door == 'yellow':
#     print('You Win!')
