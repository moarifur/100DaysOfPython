"""
---------------------------------------------------------------------------
Day05: Python Loops[Beginner]
Code Challenge 5.2: Calculate the Highest Score
Things to learn:
    - variable, input() with a list of data
    - String method: split(',') to convert str to list of str
    - for-in loop
    - Type Casting: int()
---------------------------------------------------------------------------
"""

print('Calculate the Highest Score')
highest_number = -1

# score_list = [78, 65, 89, 86, 55, 91, 64, 89]

score_list = input('Insert a list of students score:\n').split(',')
# print(score_list)
# print(type(score_list))

for score in score_list:
    if int(score) > highest_number:
        highest_number = int(score)

print(f'The highest score is: {highest_number}')

