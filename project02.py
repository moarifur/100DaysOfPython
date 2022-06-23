"""
--------------------------------------------------------------------------
Day02: Understanding Data Types and How to Manipulate Strings[Beginner]
Project02: Tip Calculator
Description: Insert total bill, percentage of tip and number of bill
split to and final result will be how much each person should pay
Steps:
    - Variable, input function
    - Type casting: string to integer
    - Calculate percentage and division
    - Print 2 decimal places
    - Formatted string literals in Python[Template literals in Javascript]
---------------------------------------------------------------------------
"""

print('Welcome to the tip calculator')
total_bill = float(input("What was the total bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
split_bill = int(input("How many people to split the bill?\n"))
final_bill = (total_bill+total_bill*tip_percentage*0.01)/split_bill
result_in_2_dec = '{:.2f}'.format(final_bill)
print(f'Each person should pay: {result_in_2_dec}')

