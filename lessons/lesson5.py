# Review

# TODO: Write a program to give me the first character of a string.
#a = str(input("Give me a string now!!!!"))
#print(a[0])
# TODO: How to get the length of a string?
#a# = input('Give me a string now!!!! ')
#print(len(a))
# TODO: Write a password checker
# - If the password has less than 6 characters, it's a weak password
# - If the password has 6 or more characters, it's a strong password
#universe. ')
# TODO: Write a program that asks for two strings and combines them.

# TODO: Write a program that asks for a number and then prints out that number plus one.

# Lesson 5: Concatenation and While loops
# Part 1: Concatenation
"""
We can't use the + operator on any two data types. We can only do:
integer + integer: adds the two integers resulting in another integer
integer + float: adds the two numbers resulting in a float
string + string: resulting in another string

We CANNOT do these:
integer + string
float + string
"""

# TODO: What will this program print out?
# print('5'+'30')
# print(3.2+30)
# print('dog' + '500')


# TODO: What will this program print out?
# print(5+29)
# print('abc + 123')

# TODO: What will # Part 2: While Loops
"""
A loop in Python is something to help us shorten our code.

There are two types of loops: while loops and for loops.

To create a while loop, you type "while", then a conditional, then a colon like this:
while x < 5:
    # Code goes here

Inside of the while loop, you write whatever you want to do for that many times. Here is an example
"""
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# Basically, this program is saying "while x is smaller or equal to 5, do this:"
# We print what x currently is, then add 1 to it.

# Example 2
# x = 0
# while x <= 100:
#     print(x)
#     x = x + 50
# print('Finished')
# TODO: What do you think the program above is going to print out? (it's ok to guess)

# Teacher TODO Problem: print all even numbers up to 100
# x = 2
# while x <= 100:
#     print(x)
#     x = x + 2

# TODO: Write a program that prints all odd numbers up to 99

# TODO: Write a program that asks for a number from the user and prints all odd numbers up to that number.
# sigmarizzler = int(input('GIVE ME A SIGMA OHIO NUMBER THAT CAN RIZZ. '))
# x = 1
# while x <= sigmarizzler:
#     print(x)
#     x += 2

# Challenge TODO: Write a program that prints this out:
# Blast off in 10
# Blast off in 9
# Blast off in 8
# ...
# Blast off in 0
# Blast off!
x = 10
while x >= 0:
    print('blast off in ' + str(x) + ' seconds')
    x -= 1
print('Blast off!')

# The end!