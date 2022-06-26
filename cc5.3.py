"""
---------------------------------------------------------------------------
Day05: Python Loops[Beginner]
Code Challenge 5.3: Adding Even Numbers
Things to learn:
    - for-in loop
    - Built-in Function: range(start, stop, step)
---------------------------------------------------------------------------
"""

print('Adding Even Numbers')
sum_of_evens = 0
for x in range(1, 101, 1):
    if x % 2 == 0:
        sum_of_evens += x
print(f'Total sum of even numbers are: {sum_of_evens}')

