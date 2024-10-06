# More practice with input() and if statements
# TODO: Make a program that asks for two numbers, then multiplies them together and prints the result
# a = int(input('give me a number. '))
# b = int(input('give me another number'))
# print(a * b)

# TODO: Make a program that asks for two numbers, and checks if the sum of the numbers is greater than 100
# a = int(input('give me a number. '))
# b = int(input('give me another number. '))
# if a + b > 100:
#     print('This number is greater than 100.')
# elif a + b < 100:
#     print('This number is less than 100.')
# else:
#     print('This is the number 100.')




# TODO: Make a program that asks for a number, then print out that number plus 1
# x = int(input('Give me a number NOW! '))
# print(x + 1)


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
36 % 5 = 1
23 % 3 = 2
19 % 6 = 1
24 % 4 = 0
16 % 13 = 3

The modulus operator is mainly used to check if a number is divisible by another number. If the modulus of two numbers is 0,
then that means that they are divisible.

Examples:
15 % 5 = 0, therefore 15 IS divisible by 5.
19 % 5 = 4, therefore 19 is NOT divisible by 5.
30 % 2 = 0, therefore 30 IS divisible by 2.
"""

# TODO: Write a program that asks for a number, and checks if the number is divisible by 5
# a = int(input('GIVE ME A NUMBER NOW!!! '))
# if a % 5 == 0:
#     print('The number is divisible by 5!!!.')
# else:
#     print('the number cannot be divided by 5. ')

# TODO: Write a program that asks for a number, and checks if the number is an even or odd number.
# a = int(input('GIVE ME A NUMBER NOW!!!! '))
# if a % 2 == 0:
#     print('This number you wrote is even.' )
# else:
#     print('This number you wrote is odd')


# More with strings
"""
Check strings
To check if something is in a string, we can use the in operator like this:
"""
# x = 'The best things in life are free!'
# print('superman' in x)

# In the program above, we check if the word 'free' is inside of the string x. It will print out True, because it is inside x.

"""
To check if something is NOT in a string, we can use the not in operator like this:
"""
# x = 'The best things in life are free!'
# print('abc' not in x) # Will print out True, because 'abc' is not in x.

# We can use if statements with the is and not operators too.
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#     print("food")
# else:
#     print('bar')
# TODO: What do you think the program above will print out?

# TODO: Write a program that asks for a string and checks if that string is in the string:
 'Isaiah lives in the USA'
 a = str(input('GIVE ME A STRING!!!! '))
 if a in 'Isaiah lives in the USA':
    print('Yes, it is in the text.' )
 else:
     print('Actually, that is not in the text.')

