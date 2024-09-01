# More practice with input() and if statements
# TODO: Make a program that asks for someone's name, then prints out how many letters the name has

# TODO: Make a program that asks for two numbers, then multiplies them together and prints the result

# TODO: Make a program that asks for two numbers, and checks if the sum of the numbers is greater than 100

# TODO: Make a program that asks for a number, then print out that number plus 1

# TODO: Make a program that asks for a temperature, and converts from celsius to fahrenheit (formula is (9/5)*C+32.)

# TODO: Add on to the last program.
# If the fahrenheit degree is over 100 degrees, print out "That is hot!".
# If the fahrenheit degree is less than 60 degrees, print out "That is cold!"
# Otherwise, print out "This is good weather."

# TODO: Make a program that asks for a number, then print out that number plus 1

# TODO: Make your own program that has at least one input(), one if statement


# Lesson 3: Modulus operator, More Strings

# The modulus operator
"""
Just like how the + operator is for addition, or the * operator is for multiplication, the modulus operator, or the % operator
is for remainder. What do I mean by that?
When dividing two numbers, the remainder is what is left over.
Example:
25 % 7 = 4, because 25 divided by 7 is 21 with a remainder of 4
13 % 2 = 1, because 13 divided by 2 is 6 with a remainder of 1

Exercises:
36 % 5 = 
23 % 3 = 
19 % 6 = 
24 % 4 =
16 % 13 =

The modulus operator is mainly used to check if a number is divisible by another number. If the modulus of two numbers is 0,
then that means that they are divisible.

Examples:
15 % 5 = 0, therefore 15 IS divisible by 5.
19 % 5 = 4, therefore 17 is NOT divisible by 5.
30 % 2 = 0, therefore 30 IS divisible by 2.
"""

# TODO: Write a program that asks for a number, and checks if the number is divisible by 5

# TODO: Write a program that asks for a number, and checks if the number is an even or odd number.



# More with strings
"""
Check strings
To check if something is in a string, we can use the in operator like this:
"""
# x = 'The best things in life are free!'
# print('free' in x)

# In the program above, we check if the word 'free' is inside of the string x. It will print out True, because it is inside x.

"""
To check if something is NOT in a string, we can use the not in operator like this:
"""
# x = 'The best things in life are free!'
# print('abc' not in x) # Will print out True, because 'abc' is not in x.

# We can use if statements with the is and not operators too.abs
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#     print("foo")
# else:
#     print('bar')
# TODO: What do you think the program above will print out?

# TODO: Write a program that asks for a string and checks if that string is in the string: 'Isaiah lives in the USA'

"""
Indexing

You can access a specific character of a string using curly braces, and then the position of that character.
Each character of a string has a position, or index. It start at 0. For example, in the string 'Hello!'

Index 0 is 'H'
Index 1 is 'e'
Index 2 is 'l'
Index 3 is 'l'
Index 4 is 'o'
Index 5 is '!'

To get the character at a specific index, you write the variable name, then put brackets [] right after. Inside the brackets,
you put the index number.

Exercise:
If there is a string name s = 'Isaiah is cool.'

What is s[3]?
What is s[0]?
What is s[6]?
What is s[7]?

Example:
"""

# s = 'Hello World'
# print(s[4])

# TODO: What do you think the program above will print out?

# TODO: Write a program that asks for someone's name, and prints out the first letter of their name.


"""
Length of string

To get the length of a string, you can use the len() function.
The len() function returns how many characters are in the string as an integer.
"""

# s = 'Hello'
# print(len(s)) # Will print out 5, because there are 5 characters in the string 'Hello'.

# TODO: Write a program that asks for a word and prints out how many letters the word has.