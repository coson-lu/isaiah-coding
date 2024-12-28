# Lesson 7: Strings 101

# Part 1: Slicing
"""
Do you remember indexing?

You use brackets like this: s[]
to get a character at a specific index of a string.

Slicing is similar, but with slicing, you can get multiple characters in a string
Lets say you have a string called x = 'Hello World' and you want to get all the characters from index 2 to index 6

'llo W'

Remember:
Index 0: H
Index 1: e
Index 2: l
Index 3: l
Index 4: o
Index 5:  
Index 6: W
Index 7: o
Index 8: r
Index 9: l
Index 10 d

Slicing works like this x[startingIndex:endingIndex + 1]

So, to get every character from index 2 to 6,
you can use slicing like this: x[2:7]

This means that I want to get a string of every character from index 2 up to but not including index 7

This will give you 'llo W'
"""

# TODO: How would you get the string: 'ell' using slicing?

# TODO: How would you get the string: ' Worl' using slicing?

# TODO: Ask the user for a string and get the first three characters from the string

# s = input('Hello, give me a string please. ')

# if len(s) > 3:
#     print(s[0:3])
# else:
#     print('You need to something bigger than three. ')


# TODO: Adding on to the previous program, add a check for whether the string the user inputted has three or more characters.
# Hi -> "You must enter more than three characters"
# Monkey -> Mon


"""
Slicing is cool, but what if I wanted to get all the characters from a certain index,
lets say 3, all the way to the end of the string?

Lets use a string called s = 'Hello World!'

I can just do s[3:len(s)]

This will give me all the characters from index 3 to the end, giving me
"lo World!"

However, Python gives us an easier way to do it

s[3:]

This will also give me
"lo World!"

You can just leave the ending index blank to go all the way to the very end.
"""

# TODO: Ask the user for a string, and print out all the characters in that string except for the first one

# a = input(' please give me a word')
# print(a[1:])




# TODO: Ask the user for a string and a number x, and print out all the characters in that string from that number x to the end
# Example: If the user inputed 'Hi Isaiah!" and 5, it would print out "aiah!"

# a = input('give me a word. ')
# b = int(input('GIVE ME A NUMBER!!! '))
# print(a[b:])


"""
You can do the same thing with the startingIndex

Given a string s = 'Hello World',
to get all the characters from the beginning to the 6th index,
you can do

s[:7]
"""


# Part 2: Modifying strings (upper and lower)

"""
You can modify strings using methods. To use methods, you can do the following
stringName = stringName.methodName()

You put a period, and then the method name.

Some methods have parameters or modifiers, and you would put them inside of the parenthesis

This class, I'll teach you two methods: The .upper() and .lower() methods.

These methods do not have any parameters.

The upper method changes everything in the string to uppercase
The lower method changes everything in the string to lowercase
"""

# TODO: Apply the .upper() method to the string s

# TODO: Apply the lower method to the string y

# TODO: Ask for a string and make the entire string capitalized and print it out

# Challenge todo: Ask for a word, and make the first letter of the word capitalized, and the rest lowercase
# Example: If I entered 'monkey', it would print out 'Monkey'
# Example: If I entered 'DOG', it would print out 'Dog'

# a = input('Gimme a word ')
# first = a[0].upper()
# rest = a[1:].lower()
# print(first + rest)


