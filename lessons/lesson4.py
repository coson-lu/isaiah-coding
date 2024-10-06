# Review

# TODO: Write a program that asks for a number and checks if that number is even or odd
# a = int(input('GIVE ME A NUMBER NOW!!!! '))
# if a % 2 == 0:
#     print('This number you wrote is even.' )
# else:
#     print('This number you wrote is odd')

# TODO: Write a program that asks for a number and prints out the remainder when that number is divided by 5
# b = int(input('GIVE ME A NUMBER NOW!!!!!! '))
# print(b % 5)
# Lesson 4: String Indexing, len() function, \n linebreaks

# Part 1: String Indexing
"""
You can get a specific character of a string with indexing.

The index of a string is the position of it. The position starts at 0.

Example:
s = "monkey"

The 0th index is the character "m"
The 1st index is the character "o"
The 2nd index is the character "n"
The 3rd index is the character "k"
etc.

TODO: In the string "monkey", which index is the "e"?
TODO: In the string "monkey", which character is at index 1?
TODO: In the string "abracadabra", which character is at index 4?

To access a character of a string using the index, we use brackets like this s[THE_INDEX],
replacing THE_INDEX with the index number of that character.
"""

# Example:
# s = 'coding'
# print(s[2])

# TODO: What do you think the program above will print out?

# TODO: Write a program that asks for a string and prints out the first letter of the string.
# a = str(input('GIVE ME A STRING!!!!! '))
# print(a[0])
# TODO: Write a program that asks for a string and prints out the second letter of the string.
# a = str(input('Give me a string!!!!!!!!!!! '))
# print(a[1])


# Part 2: len() function
"""
To get the length of a string (how many characters), you use the len() function

len is short for length.
"""
# Example:
# s = 'isaiah'
# print(len(s))

# This will print out 6, because there is 6 characters in the string.

# TODO: Write a program that asks for a string and prints out the length of it

# TODO: Write a program that asks for a password.
# - If the password is over 10 characters long, print out that it is a strong password
# - If the password is under 10 characters long, print out that it is a weak password
# pass1 = str(input('GIVE ME YOUR PASSWORD!!!!!!!!!!!! '))
# if len(pass1) >= 10:
#     print('This is a very super dooper strong password. ')
# else:
#     print('This is a weak password. ')

# TODO: Write a program that asks for a string and prints out the last character of the string
# let1 = str(input('GIVE ME A STRING NOW!!!! '))
# print(let1[len(let1) - 1])

# Part 3: \n line breaks.
"""
Lets say you are printing, but you want to print stuff on multiple lines.
You could just use another print function, but what if you wanted to do it in the same print function?

You can use the \n symbol every time you want to print on a new line.
"""
# Example:
# print('Hi Isaiah\nMy name is Coson\nHow are you?')

# Above, we use the \n symbol to have a line break.
# It will print "Hi Isaiah" on one line,
# Then, "My name is Coson" on the next line,
# Then, "How are you" on the next line.

# TODO: Write out a print function that prints anything. It must have a \n line break inside.
# print('Hello world\nMy name is Isaiah\nI really really like fortnite\nI really,really,really, like Roblox')

# TODO: Write a program that asks for two strings and concatenates them
# let1 = str(input('Give a strinng now!!!! '))
# let2 = str(input('Give me another string now!!!! '))
# print(let1 + '\n' + let2)

# TODO: Write a program that asks for a degree in Celsius and converts it to Fahrenheit. Formula (9/5)*C+32
# a = int(input('GIVE ME A DEGREE IN CELSIUS!!!! '))
# print((9/5)*a+32)
