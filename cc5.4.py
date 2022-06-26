"""
---------------------------------------------------------------------------
Day05: Python Loops[Beginner]
Code Challenge 5.4: The FizzBuzz[Job Interview Question]
Things to learn:
    - for-in loop
    - Built-in Function: range(start, stop, step)
---------------------------------------------------------------------------
"""
print('The FizzBuzz[Job Interview Question]')
for x in range(1, 101, 1):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
