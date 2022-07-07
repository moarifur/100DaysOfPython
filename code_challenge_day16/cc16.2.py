"""
-------------------------------------------------------------------------
Day16: Object Oriented Programming (OOP)[Intermediate]
Code Challenge 16.2: Practice Modifying Object Attributes and Calling Methods
Documentation: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
--------------------------------------------------------------------------
"""

from prettytable import PrettyTable

# TODO-1(Challenge-01): Create a PrettyTable object and save it
#  to a variable called table
table = PrettyTable()

# TODO-2(Challenge-02): Use docs to create a pokemon table with
#  pokemon name and type
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

# TODO-3(Challenge-03): change horizontal alignment from the center align to left align
table.align = "l"
print(table.align)

