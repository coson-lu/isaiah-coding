# Lesson 12: Lists

"""
Lists are another data type that can store multiple items

Lists are one of 4 built-in data types in Python used to store collections of data.

The other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
We'll learn about them in the future.

Lists are created using square brackets:
"""
# EXAMPLE
# thislist = ['apple', "banana", "cherry"]
# print(thislist)

# TODO: Make a variable called "week" and store the days of the week inside of the "week" variable.
# week = ['Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri', 'Sat.', 'Sun.']
# print(week)
"""
List items are ordered, changeable, and allow duplicate values.

Lists can have duplicate (more than one of the same) items.
"""
# thislist = ['apple', 'banana', 'cherry', 'banana']
# print(thislist)


"""
To get how many items are in the list, use the len() function
"""

# TODO: What will this program print out:
# cars = ['Mustang', 'Tesla', 'Ford', 'Toyota']
# print(len(cars) + 2)



"""
List items can be of any data type:
"""
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

"""
A list can contain different data types:
"""
# list1 = ["abc", 34, True, 40, "square"]



"""
List items are indexed, the first item has index [0], the second item has index [1] etc.
This is similar to indexing in strings!
"""

# thislist = ['apple', 'banana', 'cherry']
# print(thislist[0])

# TODO:
# Below there is a list variable called "animals" which is equal to ['dogs', 'cats', 'fish', 'birds', 'lions'].
# Print out the third element: 'birds'
# animals = ['dogs', 'cats', 'fish', 'birds', 'lions']
# print(animals[3])


# Negative indexing
"""
To get an item starting from the end of a list, you can use negative indexing.

The last item has an index of -1
The second to last item has an index of -2
The third to last item has an index of -3
etc.

Example:
"""
# colors = ['red', 'blue', 'green', 'yellow']
# print(colors[-1])
# print(colors[-2])

# TODO: Make a list of your favorite movies and print out the last one using negative indexing
# Movies = ['Minions', 'Hocus Pocus', 'Hocus Pocus 2']
# print(Movies[-1])



"""
You can also use slicing on lists.
When you slice a lists, it will return another list with only the items of the specified range
"""

# Example:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# This will print out "cherry", "orange", and "kiwi"

"""
Note: The slicing above will start a index 2 (included) and end at index 5 (not included).
"""



"""
You can check if an item is inside of a list using the "in" keyword
"""
thislist = ["apple",  "cherry", "orange", "kiwi", "melon", "mango"]
if 'banana' in thislist:
    print('Yes, "banana" is in the list!')
else:
    print('No, "banana" is not in the list!')


# Lets review what we just learned!

# TODO: What are lists?

# TODO: Can lists have duplicate items?

# TODO: What keyword do you use to check if something is in a list or not?

# TODO: What function do you use to get how many items are in the list?



