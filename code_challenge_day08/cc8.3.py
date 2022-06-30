"""
--------------------------------------------------------------------------------------------
Day08: Function Parameters & Caesar Cipher[Beginner]
Code Challenge 8.3: Caesar Cipher Part 1 - Encryption
Code Overview: https://replit.com/@appbrewery/caesar-cipher-1-start#main.py
Code Preview: https://repl.it/@appbrewery/caesar-cipher-1-end
*** Press 'Run'/ 'play' button to understand how does the challenge work
Things to learn:
    - Create function
    - Iteration: for-in loop
    - Conditional: if-else
    - Built-in function: range(), input(), int()
    - Keyword: global - https://tinyurl.com/4ad4mndx
    - Collection: list, string
    - String method: lower()
-----------------------------------------------------------------------------------------------
"""
print('Caesar Cipher Part 1 - Encryption')
encrypted_msg = ''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
msg = input("Type your message:\n").lower()
shifting_value = int(input("Type the shift number:\n"))


# step1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text=msg, shift=shifting_value):
    global encrypted_msg
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter) + shift
            if position > 25:
                position = position - 26
                encrypted_msg += alphabet[position]
            else:
                encrypted_msg += alphabet[position]
    print(f'The decoded text is {encrypted_msg}')


if direction == 'encode':
    encrypt()
elif direction == 'decode':
    print('Not yet!')
else:
    print('What are you doing??')

