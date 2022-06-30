"""
--------------------------------------------------------------------------------------------
Day08: Function Parameters & Caesar Cipher[Beginner]
Project08: Caesar Cipher
Code Overview:
Code Preview: https://replit.com/@appbrewery/caesar-cipher-4-end
*** Press 'Run'/ 'play' button to understand how does the challenge work
-----------------------------------------------------------------------------------------------
TODO-1: Import and print the logo from art.py when the program starts.
TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    e.g. Try running the program and entering a shift number of 100.
TODO-3: What happens if the user enters a number/symbol/space?
TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
    e.g. Type 'yes' if you want to go again. Otherwise type 'no'

"""
# TODO-1
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]


# Caesar Cipher Program
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    # Check Direction
    if cipher_direction == "decode":
        shift_amount *= -1
    elif cipher_direction == "encode":
        pass
    else:
        print('What are you doing? You are given wrong direction')
        return

    for letter in start_text:
        # TODO-3
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter

    print(f"Here's the result: {end_text}")


# TODO-4
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2
    shift %= 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Check Decision
    decision = input("Do you want to restart the cipher program?\n").lower()
    if decision == 'yes':
        pass
    elif decision == 'no':
        print('Goodbye!')
        break
    else:
        print('What are you typing?')


"""
--------------------------------------------------------------------
Things you'll learn:
    - Create function
    - Iteration: for-in, while loop
    - Conditional: if-else
    - Built-in function: input(), int()
    - Statement/ Keyword: break, pass - https://tinyurl.com/3tkje3yn
    - Collection: list, string
    - String method: lower()
---------------------------------------------------------------------   
"""
