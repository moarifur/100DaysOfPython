"""
--------------------------------------------------------------------------------------------
Day08: Function Parameters & Caesar Cipher[Beginner]
Code Challenge 8.5: Caesar Cipher Part 3 - Reorganising our Code
Code Overview: https://replit.com/@appbrewery/caesar-cipher-3-start#main.py
Code Preview: https://replit.com/@appbrewery/caesar-cipher-3-end
*** Press 'Run'/ 'play' button to understand how does the challenge work
Things to learn:
    - Create function
    - Iteration: for-in loop
    - Conditional: if-else
    - Built-in function: input(), int()
    - Collection: list, string
    - String method: lower()
-----------------------------------------------------------------------------------------------
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1
    elif cipher_direction == "encode":
        pass
    else:
        print('What are you doing? You are given wrong direction')
        return

    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
