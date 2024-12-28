# Review
# What is slicing?

# What are string methods?

# What string methods do did you learn last class? What do they do?

# TODO: Ask the user for a string, and make the whole string capitalized
# a = input('Give me a string please. ')
# print(a.upper()%)

# TODO: Ask the user for a string, and make just the first letter capitalized
# a = input('give me a string NOW!!!! ')
# first = a[0].upper()
# end = a[1:].lower()
# print(first + end)


# Lesson 8: string methods

# Part 1: The .strip() method
"""
The .strip() removes whitespace from eitherside of a string

For example, if there was a string s = "   my name is isaiah       ",
the .strip() method would make it into "my name is isaiah"

The .strip() method also removes new lines.

If I have a string "  i like apples  \n\n", it would make it into "i like apples"

"""

# TODO: Remove apply the .strip() method to x, and print it out
# x = '\nI like oranges  \n '
# print(x.strip())


# Part 2: The .replace() method
"""
Remember when I said that some methods have modifiers or parameters that go inside the parenthesis?

The .replace() method is one of those methods!

The .replace() method replaces all instances of a string with another string.
The first parameter is the string you want to be replaced
The second parameter is the string you want to replace it with

"""
# Example 1:
# x = 'Hello World'
# x = x.replace('H', 'J')
# print(x)

# Example 2:
# x = 'Hello world'
# x = x.replace('o', 'ISAIAH')
# print(x)

# Example 3:
# x = 'I like dogs and dogs are cool'
# x = x.replace('dogs', 'cats')
# print(x)

# TODO: Ask the user for a string, and replace all the 'e's with 'o's and print it out
# x = input('Give me a string now! ')
# print(x.replace('e', 'o'))

# TODO: Ask the user for a string, and delete all of the 'i's in the string and print it out
# x = input('GIVE ME A STRING PLEAAEAEAEAEAEASE!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ')
# print(x.replace('i', ''))


# Part 3: The .count method
"""
The .count() method

The .count() method returns the number times a specific value appears in the string
It takes in one parameter: the specified value
"""

# Example:
# x = 'Hello World!'
# print(x.count('l'))

# TODO: Ask the user for a string and count the number of e's in the string and print it out
# x = input('GIVE COSON A STRING NOW!!!!!!!!!!!!!! ')
# print(x.count(' '))

# TODO: Ask the user for a string and count the number of vowels in the string and print it out
# Example: If the string was 'i like apples', it would print out 5
# x = input('Give me string now please. ')
# print(x.count('a') + x.count('e') + x.count('i') + x.count('o') + x.count('u'))
# s = 1 + 2 + 3 + 4
# print(s)


# Challenge TODO: Ask the user for a string and count the number of consonants in the string and print it out
# Example: If the string was 'i like apples', it would print out 6



