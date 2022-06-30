"""
-------------------------------------------------------------------------
Day09: Dictionaries, Nesting and the Secret Auction
Code Challenge 9.2: Travel Log Program
Code Overview: https://replit.com/@appbrewery/day-9-2-exercise#README.md
Code Preview: https://repl.it/@appbrewery/day-9-2-solution
*** Press 'Run'/ 'play' button to understand how does the challenge work
--------------------------------------------------------------------------
TODO: Write the function that will allow new countries to be added to the travel_log.

"""

# List of dictionary
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

# print(travel_log[0]['country'])


# TODO:
def add_new_country(name, visit_count, cities_visited):
    # new_country = {}
    #     new_country['country'] = name
    #     new_country['visits'] = visit_count
    #     new_country['cities'] = cities_visited

    new_country = {
        'country': name,
        'visits': visit_count,
        'cities': cities_visited
    }

    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

"""
------------------------------------------------------------------------------
Things you'll learn:
    - Collection: dictionary, list
    - Create Dictionary
        - https://www.geeksforgeeks.org/python-dictionary/ 
        - https://docs.python.org/3/tutorial/datastructures.html#dictionaries
        - https://www.w3schools.com/python/python_dictionaries.asp
    - User defined function: add_new_country()
    - List Method: append()
---------------------------------------------------------------------------------  
"""
