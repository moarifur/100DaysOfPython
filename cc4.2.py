"""
---------------------------------------------------------------------------
Day04: Randomisation and Python Lists[Beginner]
Code Challenge 4.2: Banker Roulette - Who will pay the bill
Things to learn:
    - Variable, input()
    - String Method: split() convert a string to a list
    - List Method: len()
    - Random Module: randint()
    - conditionals: if, elif
---------------------------------------------------------------------------
"""

import random

names = input("Give me everybody's name, seperated by comma\n")
name_list = names.split(',')
random_number = random.randint(0, len(name_list)-1)

person_who_will_pay = name_list[random_number]
print(f'{person_who_will_pay} is going to buy the meal today!')

# print(random_number)
# if random_number == name_list.index(name_list[random_number]):
#     print(f'{name_list[random_number]} is going to buy the meal today!')
