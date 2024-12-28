# Removing items from lists

"""
What method do you use to add an item to a list? (write it on line 5)


There are two methods to remove an item to a list

Today, I'll teach you the first method.
The first method is the .remove(). This method takes in one value: the specific item you want to remove from the list.

Example 1:
"""
# fruits = ['apple', 'banana', 'cherry']
# fruits.remove('banana')
# print(fruits)

"""
Example 2:
"""
# numbers = [33, 8, 42, 35]
# numbers.remove(42)
# print(numbers)

# TODO: Here is a list called a_list. Remove the color 'orange' from the list
# a_list = ['red', 'yellow', 'orange']
# a_list.remove('orange')

# TODO: Here is a list called primes. Remove the numbers 4 and 6 from the list
# primes = [2, 3, 4, 5, 6, 7]
# primes.remove('4').remove('6')

"""
Can lists have duplicates?


Say we have a list called numbers, and it has 3 4s. What do you think the program below will print out?
"""
# numbers = [5, 4, 9, 10, 4, 4]
# numbers.remove(4)
# print(numbers)










"""
The .remove() function only removes the FIRST occurance of an item.
Therefore, the program above will print out [5, 9, 10, 4, 4]
"""



# Mini quiz
# Instructions:
# There will be a series of programs. Your job is to figure out what the program will print out.
# Write your answer on the comment below the program. You have 15 minutes to complete this.
# Warning: Some of them are designed to trick you! Be careful!

"""
Example:
lst = [1, 1, 2, 3, 5, 8, 13]
lst.remove(5)
print(lst)
"""
# Answer: [1, 1, 2, 3, 8, 13]



"""
Program 1:
a = ['iphone', 'macbook', 'ipad']
a.remove('iphone')
print(a)
"""
# Answer: ['macbook', 'ipad']



"""
Program 2:
a = [5, 10, 10, '10']
a.remove(10)
print(a)
"""
# Answer: [5, 10, '10']



"""
Program 3:
lst = ['pencil', 'eraser', 'ruler']
lst.remove('Pencil')
print(lst)
"""
# Answer: ['pencil', 'eraser', 'ruler']



"""wrong
Program 4:
lst = [50, 20, 30]
lst[1] = lst[1] + 10-
print(lst[0] - lst[1])
"""
# Answer: [20, 20, 20]
# New Answer: 20



"""
Program 5:
lst = ['pencil', 'eraser', 'ruler']
lst[0] = lst[0] + 's'
print(lst)
"""
# Answer: ['pencils', 'eraser', 'ruler']



"""
Program 6:
a_list = [9, 10, 11]
a_list.append(12)
a_list.remove(11)
print(a_list)
"""
# Answer: [9,10,12]



"""
Program 7:
a_list = ['hello!']
a_list.remove('hello!')
print(a_list)
"""
# Answer: []



"""wrong
Program 8:
a_list = ['bed', 'couch', 'tv']
a_list = [1, 2] + a_list
print(a_list)
"""
# Answer: ['bed', 'couch', 'tv', 1, 2]
# New Answer: [1, 2, 'bed', 'couch', 'tv']

+
"""
Program 9:
fives = [5, 10, 15, 20, 25]
print(fives[1:] + [1, 2, 3])
"""
# Answer: [10, 15 ,10, 25, 1, 2, 3]



"""wrong
Program 10:
a_list = ['good', 'bad', 'evil']
print(a_list[0] + a_list[1] + 'hello')
"""
# Answer: ['good', 'bad', 'hello']
# New Answer: 'goodbadhello'


# Score: 7/10

