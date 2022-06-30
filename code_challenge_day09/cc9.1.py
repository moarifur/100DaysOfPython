"""
--------------------------------------------------------------------------------------------
Day09: Dictionaries, Nesting and the Secret Auction
Code Challenge 9.1: Grading Program
Code Overview: https://replit.com/@appbrewery/day-9-1-exercise#README.md
Code Preview: https://replit.com/@appbrewery/day-9-1-solution
*** Press 'Run'/ 'play' button to understand how does the challenge work
-----------------------------------------------------------------------------------------------
TODO-1: Create an empty dictionary called student_grades.
TODO-2: Write your code below to justify the grades to student_grades.
    e.g.
        - Scores 91 - 100: Grade = "Outstanding"
        - Scores 81 - 90: Grade = "Exceeds Expectations"
        - Scores 71 - 80: Grade = "Acceptable"
        - Scores 70 or lower: Grade = "Fail"

"""
# TODO-1
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

# TODO-2
for key in student_scores:
    if 91 <= student_scores[key] <= 100:
        print(f"{key}: Outstanding")
    elif 81 <= student_scores[key] <= 90:
        print(f"{key}: Exceeds Expectations")
    elif 71 <= student_scores[key] <= 80:
        print(f"{key}: Acceptable")
    elif student_scores[key] <= 70:
        print(f"{key}: Fail")


"""
------------------------------------------------------------------------------
Things you'll learn:
    - Collection: dictionary
    - Create Dictionary
        - https://www.geeksforgeeks.org/python-dictionary/ 
        - https://docs.python.org/3/tutorial/datastructures.html#dictionaries
        - https://www.w3schools.com/python/python_dictionaries.asp
    - Iteration: for-in
    - Conditional: if-else
---------------------------------------------------------------------------------  
"""