"""
-------------------------------------------------------------------------
Day10: Functions with Outputs
Code Challenge 10.1: Days in Month
Code Overview: https://replit.com/@appbrewery/day-10-1-exercise#README.md
Code Preview: https://repl.it/@appbrewery/day-10-1-solution
*** Press 'Run'/ 'play' button to understand how does the challenge work
--------------------------------------------------------------------------
TODO-1: is_leap_year(year) to check whether there is a 'leap year' or not
TODO-2: days_in_a_month(year, month) returns how many days have in a month

"""


# TODO-1
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO-2:
def days_in_a_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        month_days[1] = 29
    return month_days[month-1]


given_year = int(input('Enter a Year: '))
given_month = int(input('Enter a month: '))
print(days_in_a_month(given_year, given_month))

"""
------------------------------------------------------------------------------
Things you'll learn:
    - User defined function: is_leap_year(year), days_in_a_month(year, month) 
    - Collection: list
    - Conditional: if-else
---------------------------------------------------------------------------------  
"""
