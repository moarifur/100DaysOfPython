"""
--------------------------------------------------------------------------------------------
Day08: Function Parameters & Caesar Cipher[Beginner]
Code Challenge 8.2: Prime Number Checker
Code Overview: https://replit.com/@appbrewery/day-8-2-exercise#README.md
Code Preview: https://repl.it/@appbrewery/day-8-2-solution
*** Press 'Run'/ 'play' button to understand how does the challenge work
Things to learn:
    - Create function
    - Iteration: for-in loop
    - Conditional: if-else
    - Built-in function: range()
-----------------------------------------------------------------------------------------------
"""
print('Prime Number Checker')
number = int(input('Please enter a number: '))


def prime_number(num=number):
    flag = 0
    for n in range(2, num - 1):
        if num % n == 0:
            flag += 1
    if flag == 0:
        return 'a prime number'
        # print("it's a prime number!")
    else:
        return 'not a prime number'
        # print("It's not a prime number!")


print(f"The number given by the user is: {number} which is {prime_number()}")
