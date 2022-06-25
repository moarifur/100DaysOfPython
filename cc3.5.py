"""
-------------------------------------------------------------------------------------------------------
Day03: Control Flow and Logical Operators[Beginner]
Code Challenge 3.5: Love Calculator
Things to learn:
    - Variable, input function, type casting
    - String function: count(), lower()
    - Conditionals: if-elif-else
    - String formatting: string literals
--------------------------------------------------------------------------------------------------------
"""

print('Love Calculator')
female = input("Insert the gf name:\n").lower()
male = input("Insert the bf name:\n").lower()

true = male.count('t') + female.count('t') + male.count('r') + female.count('r') + \
    male.count('u') + female.count('u') + male.count('e') + female.count('e')
love = male.count('l') + female.count('l') + male.count('o') + female.count('o') + \
    male.count('v') + female.count('v') + male.count('e') + female.count('e')

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}')

# print(f'BuzzFeed said that your love in percentage is: {true}{love}%')

# ---Sample name-----
# gf: Kim Kardashian
# bf: Kanye West
# score: 42
#