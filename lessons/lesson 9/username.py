"""
Goal: Help someone create their online username by combining their first and last names!

Description:
 - Have the user input their first name, and then have them input their last name
 - Print out a string that contains the first three letters of the first name, and the last three letters of their last name.
 - If either name has less than three letters, use the entire name

Examples:
 - If the user inputted "Isaiah" for the first name, and "Lin" for the last name, you should output "Isalin" ("Isa" and "lin")
 - If the user inputted "Joshua" for the first name, and "Smith" for the last name, you should output "Josith" ("Jos" and "ith")
 - If the user inputted "Will" for the first name, and "James for the last name, you should output "Wilmes" ("Wil" and "mes")
 - If the user inputted "Coson" for the first name, and "Lu" for the last name, you should output "Coslu" ("Cos" and "lu")

You'll probably need to use:
 - Slicing
 - Concatenation

Feel free to ask if you are stuck or need hints!
"""
# Write your code here:

# The input is already done for you
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print(first_name[0:3] + last_name[len(last_name) - 3:])

