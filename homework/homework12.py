# What is an array? (answer in a comment)
# it is a list but called an array 
# What can you store in an array? (answer in a comment)
# you can store integers, strings, anf floats
# How do you check if an item is inside of an array? (answer in a comment)
# in
# Here's an array called "arr1". The next few TODOS will have you access it
arr1 = ['apples', 'bananas', 'cherries']

# TODO:  Print out "bananas" using indexing. Then, print out "cherries" using negative indexing
print(arr1[1])
print(arr1[-1])
# TODO: Print out the length of the arr1.
print(len(arr1))

# TODO: Add another fruit to arr1.
arr1.append('mangosteen')

# TODO: Change the 0th index ("apples") into a different fruit.
arr1[0] = 'cucumber'

# TODO: Print out the concatenation of arr1 and this list: ['dogs', 'cats', 'dolphins']
print(arr1 +  ['dogs', 'cats', 'dolphins'] )
