"""
---------------------------------------------------------------------------
Day04: Randomisation and Python Lists[Beginner]
Code Challenge 4.1: Find 'Heads' or 'Tails'
Things to learn:
    - Variable
    - conditionals: if, elif
    - Module: random - randint()
---------------------------------------------------------------------------
"""

import random

random_number = random.randint(0, 1)

if random_number == 0:
    print('Tails')
elif random_number == 1:
    print('Heads')
