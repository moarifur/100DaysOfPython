"""
---------------------------------------------------------------------------
Day06: Python Functions & Karel[Beginner]
Code Challenge 6.2: Reeborg's World Hurdles-2 Challenge
Game URL: https://tinyurl.com/mtc3z6wa
Things to learn:
    - while loop
    - 'not' keyword
    - Create a function: def function_name():
*** Put/ open this code to the python code console in the game dashboard
---------------------------------------------------------------------------
"""


def jump():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()


while not at_goal():
    jump()
