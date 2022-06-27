"""
---------------------------------------------------------------------------
Day06: Python Functions & Karel[Beginner]
Code Challenge 6.3: Reeborg's World Hurdles-3 Challenge
Game URL: https://tinyurl.com/mryde8rx
Things to learn:
    - Create a function: def function_name():
    - while loop
    - 'not' keyword
    - if-else
*** Put/ open this code to the python code console in the game dashboard
---------------------------------------------------------------------------
"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()