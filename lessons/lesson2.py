# Review

# 1. print() function
# What does the print() function do?
# TODO: Use the print() function to display the name of your school on the line below
# print("Coastline Christian Schools")

# 2. Variables
# What are variables?
# Can variables change?
# TODO: create a named pet and make it equal to "dog" below 
# pet = "dog"

# TODO: print the pet variable out below
# print(pet)

# TODO: change the pet variable to "cat" and then print the variable out again below
# pet = "cat"
# print(pet)

# 3. Data types
# What are the three data types we learned?
# Describe what each data of the data types are.t




# LESSON 2 - Casting, Operators, Booleans, if statements, String Basics, the input() function
# This lesson, we'll be looking into more complicated concepts than last time.

# Part 1: Casting
# In python, it is possible for a variable of one data type to change to another data type. This is called casting.

# Casting is done with functions. There are three casting functions that we'll learn today: int(), float(), str()

# int() function: constructs an integer number from another integer, a float (removes decimal points), or a string (provided that the string is a whole number)
# Examples:
x = int(3) # x will be 3
y = int(4.73) # y will be 4 (it removes the decimals)
z = int("13") # z will be 13%

# float() function: constructs a float number from an integer (adds a .0), another float, or a string (provided that the string is a number)
# Examples:
x = float(1) # x will be 1.0
y = float(5.32) # y will be 5.32
z = float('13.29') # TODO: What do you think z will be?
w = float('34') # TODO: Trick question: What do you think w will be?

# str() function: constructs a string from many data types including strings, integers, and floats
# Examples:
x = str(5) # x will be "5"
y = str(8.16) # TODO: What do you think y will be?
z = str("52") # TODO: What do you think z will be?
w = str(-39) # TODO: What do you think w will be?

# CASTING PRACTICE:
# Here is a variable named n that is an integer
n = 32
# TODO: Turn n into a float on the line below with the float() function
n = float(n)

# TODO: Now turn n into a string on the line below
n = str(n)

# TODO: use the print() function to print the type of n. (hint: use the type() function)



# Part 2: Operators
# In Python, you can use operators. Operators are used to perform operations. You can use operators on almost every single data type.
# For now, we'll just be focusing on operators with integers.

# Integer operators:
# To add, you use the + operator
# To subtract, you use the - operator
# To multiply, you use the * operator
# To divide, you use the / operator
# To group, use parentheses ()

# Example:
x = 3 + 10
# Here, we use the + operator to add 3 + 10. x has a value of 13.
# Python follows order of operations
x = 10 + 5 * 2 # Will have be 20, because 10 + 5 * 2 = 10 + 10 = 20

# If we wanted to do 10 + 5 first, we would use parentheses to group
x = (10 + 5) * 2

# We can also use operators on variables too.
# Example:
# Here, we have two variables:
x = 10
y = 2
# print(x + y) # We can use the + operator to add them together
# TODO: try printing the difference of x and y with the - operator below
x = 5000
y = 11
# print(x - y)

# TODO: try printing the product of x and y with the * operator below
# print(x * y)

# TODO: try printing the quotient of x and y with the / operator below
# print(x / y)

# CHALLENGE: try to assign x a value of 5 more than x. Then, print out x to see if it worked


# CHALLENGE: try to assign y a value of 10 less than y. Then, print out y to see if it worked


# In python, we assign values to variables using the past value of the variable so often, python gave us a way to shorten it.
# It's hard to explain, so let me just show you.


# Part 3: Booleans
# Remember when we learned about three data types: integers, floats, and strings?
# There's another data type called booleans.
# What is a boolean? Any guesses?

# A boolean's value can be either True or False. At first, this might not seem very useful, but it can be very helpful at times!
b = True # b is a variable whose value is True. It is a boolean.

# TODO: create a variable named has_pets and give it a value of False
has_pets = False

# Just like how there are operators with integers, there are also operators with booleans.
# They are called comparison operators.

# Preview:
# print(3 > 5) # prints a boolean value of False, because 3 is less than 5.

# Boolean operators:
# == - Equal to
# != - Not equal to
# > - Greater than
# < - Less than
# >= - Greater than or equal to
# <= - Less than or equal to.

# You can use the boolean operators with variables or values.
# Example:
x = 3
y = 6

# TODO: What do you think this will print out:
# print(x == y)

# TODO: What do you think this will print out:
# print(3 >= 4)

# TODO: What do you think this will print out:
# print(32.3 <= 32.3)

# TODO: What do you think this will print out:
# print(8 != -5)

# TODO: Below, make two variables and assign them a value of any integer. Then, use a boolean operator to compare them and print it out.
u = 890
h = 70


# Part 3: if statements
# if statements are used to only do something if a certain condition is met.
# Example:
# a = 20
# b = 1
# if b > a:
#   print("b is greater than a")

# In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 20, and b is 5000, we know that 5000 is greater than 20, and so we print to screen that "b is greater than a".

# To write an if statment, you write if, then a space, then the conditional boolean statement, then a colon:,    then on a new line that is indented you write whatever you want to do if the boolean condition is met.
# Example:
if 7 == 9:
  print('The statement above is true')
# In the example above, we do not print anything, because 7 is not equal to 9

# if 32 >= 32:
#   print('Hello Isaiah')
#   print('My name is Coson')
#   x = 90
# In this example, it does print out stuff, because the boolean is True.

# IMPORTANT: When writing if statements. You HAVE to indent the stuff after the if statement. This is how python knows what you want to put inside the if statement.

# WRONG EXAMPLE:
# if 5 > 3:
#   print("5 is greater than 3")

# If we run this, it will give us a traceback error, because we did not indent.

# Practice:
# TODO: Make any if statement and print something inside of that if statement
# if 5.09 >= 5.09:
#   print("ErrorError")


# elif
# writing elif is Python's way of saying "if the previous conditions were not True, then try this condition"
# Example:
# x = 4
# if x == 4:
#   print('x is equal to 4')
# elif x == 5:
#   print('x is equal to 5')
# In the example above, x is equal to 5, so the first condition is not true, but the second condition is, so we print out "x is equal to 5".
# TODO: Try changing the x to 4 and run the program!

# You can have multiple if and elif statements
# x = 32
# if x > 100:
#   print('x is bigger than 50')
# elif x > 10:
#   print('x is bigger than 10, but less than 100')
# elif x > 5:
#   print('x is bigger than 5, but less than 10')
# What do you think the program above will print out?

# The program above is cool and all, but what if we wanted to print something out if x is none of those conditions?
# We can use else.
# Writing else is Python's way of saying, "If none of the operations above are True, then do this"

# Example:
# x = 5
# y = 3
# if x + y == 500:
#   print('The sum of x and y is 500')
# elif x + y == 400:
#   print('The sum of x and y is 400')
# elif x + y == 100:
#   print('The sum of x and y is 100')
# else:
#   print('The sum of x and y is not 500, 400, or 100')

# TODO:
x = 100
# Write a program that checks if x is greater than 100, equal to 100, or less than 100.
# if x == 100:
#   print("x is equal to 100")
# elif x > 100:
#   print("x is greater than 100")
# else:
#   print('x is less than 100')




# Part 4: String Basics
# You learned about strings last lesson. To recap, strings can anything. They are typically used to store words and sentences. To create a string, you have to put quotations around the thing you want to be a string.
# Below, we create a variable named s, and it's value is "This is a string"
s = "This is a string"

# Double quotes or single quotes?
# The quotations around strings can either be double quotes like this: ", or single quotes like this '. It doesn't matter as long as the starting quote is the same type as the ending quote
# Some programmers like to use double quotes, and some like to use single quotes
# It is of personal preference.
# I personally like the use single quotes.

# Concatenation
# Concatenation is just a fancy word for the joining of two things.
# We can join two strings together through concatenation. We use the + operator on strings.
# Example:
x = 'abc'
y = 'defghijk'
z = x + y
# Here, we have x, which is equal to 'abc', y, which is equal to 'def', and z, which is equal to x + y.
# When you add two strings, they get concatentated, putting them both into one string.
# In the example above, z concatenates x and y, so it becomes 'abcdef'.

# TODO: Print out z below.
# print(z)

# TODO: Make two strings and print out the concatenation of them.
# a = 'abcdefghijklmn'
# b = 'opqrstuvwxyz'
# c = a + b
# print(c)

# Concatenation of self.
s = 'foot'
s = s + 'ball'
# Above, s is equal to 'foo'. Then, we concatenated s and 'bar', so s is now 'foobar'
# TODO: print out s.
# print(s)

# Remember how for integers, if we are doing
# x = x + 5
# We can just shorten it to
# x += 5

# We can do the same thing for strings!
# Example:
s = 'abc'
s = s + 'xyz'
# TODO: What do you think s will equal now?
# s = s + 'xyz' is the same as
s += 'xyz'

# The += operator is the primary way we add stuff to strings.

# Length of string
# You can get how many characters a string is is using the len() function.
# Example:
# s = 'supercalifragiexpialidocious'
# x = len(s)

# TODO: What do you think the value of x is?
# TODO: Below, print out x to see if you are correct.
# print(x)


# Part 5: the input() function
# The input() function is what allows you to interact with the user.
# You always assign inputs to the a variable. Inside the input() function goes a string which is what you want to say to the user.
# Then, the program waits for the user to say type something in. When the user presses enter, it continues to run the program. The variable you assigned the input() function to is now whatever the user typed in in the form of a string.

# Example:
# x = input('What is your favorite book? ')
# print('Your favorite book is ' + x)
# In the example above, we ask what the user their favorite book is. Then, we use concatenation to combine 'Your favorite book is' with whatever the user typed in.

# TODO: In the line below, ask the user what their favorite movie is, and then print it out.
# s = input('What is your favorite movie? ')
# print('Your favorite movie is ' + s)

# TODO: In the line below, ask the user what their name is, and then tell them hello with their name.
# a = input('What is your name? ')
# print('Hello, ' + a)

# Remember, the input() function always returns back what the user inputed as a string. This means that even if the user entered an integer, it was still be an integer inside of a string.

# If we want the value as an integer, what do you think we would do with the variable? (hint: we learned it in this lesson already)

# TODO: Below, change the favorite_number variable into an integer and print out the number plus 10.

# In-class assignment: Simple addition calculator
# Instructions: ask the user for two numbers, then print out the numbers added together. Ask questions if you need any help
# a = input('Give me a number. ')
# b = input('Give me another number. ')
# a = int(a)
# b = int(b)
# c = a * b
# print(c)
