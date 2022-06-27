"""
----------------------------------------------------------------------------------
Day05: Python Loops[Beginner]
Project05: PyPassword Generator
Description: User defined the size of the password and how many letters,
symbols & numbers are included in the password and then create a whole new
password with random module.
Steps:
    - Variable, input function, type casting
    - Iteration: for-in loop
    - Random Module: randint(start, end), shuffle()
    - List Method: append()
    - Built-in Method: input(), range(), len()
    - String Method: Formatted string literals, join() - to convert list to string
------------------------------------------------------------------------------------
"""
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
           ]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password = []

print('Welcome to PyPassword Generator!')
letters_counter = int(input("How many letters would you like in your password?\n"))
symbols_counter = int(input("How many symbols would you like?\n"))
numbers_counter = int(input("How many numbers would you like?\n"))

for x in range(0, letters_counter):
    rand = random.randint(0, len(letters)-1)
    password.append(letters[rand])

for x in range(0, symbols_counter):
    rand = random.randint(0, len(symbols)-1)
    password.append(symbols[rand])

for x in range(0, numbers_counter):
    rand = random.randint(0, len(numbers)-1)
    password.append(numbers[rand])

random.shuffle(password)
shuffled_pass = ''.join(password)
print(f'Here is your password: {shuffled_pass}')
# print(type(shuffled_pass))
