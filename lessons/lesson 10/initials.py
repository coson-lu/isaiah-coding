"""
Goal: Given two names, print out the initials of the person!

Task:
 - Ask the user for their first, and last name (already done for you)
 - Print out the user's initals

Examples:
 - If the user inputs "Coson" for their first name and "Lu" for their last name, print out "C. L."
 - If the user inputs "Isaiah" for their first name and "Lin" for their last name, print out "I. L."
 - If the user inputs "John" for their first name and "Doe" for their last name, print out "J. D."

You will probably need to use:
 - Indexing
 - Concatenation
"""

x = input('What is your first name? ')
y = input('What is your last name? ')
x = x[0]
y = y[0]


print(x.upper() + '. ' + y.upper() + '.')