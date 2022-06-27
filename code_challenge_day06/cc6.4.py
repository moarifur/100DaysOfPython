"""
---------------------------------------------------------------------------
Day06: Python Functions & Karel[Beginner]
Code Challenge 6.4: Reeborg's World Hurdles-4 Challenge
Game URL: https://tinyurl.com/ef6a323z
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
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()