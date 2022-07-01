"""
-------------------------------------------------------------------------
Day09: Dictionaries, Nesting and the Secret Auction
Project09: Blind Auction Program
Code Overview:
Code Preview: https://replit.com/@appbrewery/blind-auction-completed
*** Press 'Run'/ 'play' button to understand how does the challenge work
--------------------------------------------------------------------------
TODO: Write the function that will.........................

"""
# ---------- Complex Version: Correct answer with dictionary --------------
import os
import time

from art import logo

# Print logo
print(logo)
bids = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    highest_bidder = ''

    # bidding_record:
    for bidder in bidding_record:
        if highest_bid < bidding_record[bidder]:
            highest_bid = bidding_record[bidder]
            highest_bidder = bidder

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


while True:
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: $"))
    check_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

    bids[name] = bid

    if check_bidders == 'yes':
        os.system('cls')

    elif check_bidders == 'no':
        find_highest_bidder(bids)
        time.sleep(3.5)
        break


"""
------------------------------------------------------------------------------
Things you'll learn:
    - Collection: dictionary
    - Create Dictionary
        - https://www.geeksforgeeks.org/python-dictionary/ 
    - Conditional: if-else
    - Iteration: for-in loop in dictionary, infinite while loop with break    
    - User defined function: find_highest_bidder(dictionary)
    - Module: os, time, art(user defined)
    - os method: os.system('cls') - for clearing screen in console
    - time method: time.sleep(time in minutes)
---------------------------------------------------------------------------------  
"""

# ---------- Simpler Version: Correct answer without dictionary --------------
# from art import logo
#
# # Print logo
# print(logo)
# highest_bidder = ''
# highest_bid = 0
#
# while True:
#
#     name = input('What is your name?: ')
#     bid = int(input("What's your bid?: $"))
#
#     if bid > highest_bid:
#         highest_bid = bid
#         highest_bidder = name
#
#     check_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
#     # if bidders == 'yes':
#     #     clear()
#     if check_bidders == 'no':
#         break
#
# print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
