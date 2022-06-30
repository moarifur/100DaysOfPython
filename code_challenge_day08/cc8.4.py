"""
--------------------------------------------------------------------------------------------
Day08: Function Parameters & Caesar Cipher[Beginner]
Code Challenge 8.4: Caesar Cipher Part 2 - Decryption
Code Overview: https://replit.com/@appbrewery/caesar-cipher-2-start#main.py
Code Preview: https://replit.com/@appbrewery/caesar-cipher-2-end
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
print('Caesar Cipher Part 2 - Decryption')
decrypted_msg = ''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
msg = input("Type your message:\n").lower()
shifting_value = int(input("Type the shift number:\n"))


def decrypt(text=msg, shift=shifting_value):
    global decrypted_msg
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter) - shift
            if position < 0:
                position = position + 26
                decrypted_msg += alphabet[position]
            else:
                decrypted_msg += alphabet[position]
    print(f'The decoded text is {decrypted_msg}')


if direction == 'encode':
    print('Done in cc8.3!')
elif direction == 'decode':
    decrypt()
else:
    print('What are you doing??')
