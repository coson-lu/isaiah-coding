# Remember while loops?

# Lets do some review:
"""
Loops in programming are bits of code that run repeatedly a couple times

It could run repeatedly 5 times. 10 times. 100 times. 100,000 times. Or even infinitely!!

There are two types of loops in python: while and for loops.
"""

"""
We'll first learn about while loops today, and for loops in the future.

While loops always have a condition and an action.
Repeat: "a condition and an action"
Now repeat it 3 more times.
"""

"""
Before we start coding. Let me give you a real life example.

Drinking water is an example of a while loop!
The condition is: While the glass is not empty,
The action is: Take a gulp of water

Walking to somewhere is also a while loop!
The condition: While you're not already at your destination,
The action is: Take another step

Eating until you're full is also an example of a while loop:
The condition: While you're not yet full,
The action: Take another bite of your food
"""

# TODO: Come up with your own real life example below!
"""
your example: Gaming until you win is another while loop:
condition: When you didn't win
action: keep playing
"""

"""
Coding while loops are really simple!

You just type "while", then the CONDITION, then a colon.
After indenting write out the ACTION

Example:
cc
while condition:
    # action
"""

# Example:
# count = 10
# while count >= 0:
#     print(count)
#     count -= 1

# This program is saying
# Condition: while the variable "count" is less than or equal to 5
# Action: print out the count and add one to count

# Now run the program!

"""
Important!

There will (almost) always be a variable inside of our condition!
This variable HAS to change inside of the while loop.

If it doesn't change, then it won't affect the condition, and therefore it will run FOREVER!!

In the program above, the variable that changes is the "count" variable.
Each time the while loop runs, it adds one to the count.
"""


# Example 2:
# countdown = 5
# while countdown > 0:
#     print(str(countdown) + '!')
#     countdown -= 1
# print('Blast off!')

# This program is saying
# Condition: while the variable "countdown" is greater than 0
# Action: print the countdown and then an exclamation mark and then subtract one from countdown
# After the while loop is done, it prints out "Blast off!"

# Run the program!

# TODO: Ask the user for a number. Then, make a program that starts from one and counts to that number
# Example: If the user inputted 9, the program would count from 1 to 9

# TODO: Ask the user for a number. This time, make a program starts from one and counts every other number up to that number
# Example: If the user inputted 9, the program would print out this:
"""
1
3
5
7
9
"""





"""
The action in the while loop can be anything!

We can get really creative with input()
"""
# Example:

secret_word = 'monkey'
guess_counter = 0
while guess_counter < 5:
    guess = input('Enter your guess: ')
    if guess == secret_word:
        print('You got it correct!')
        break
    else:
        print('Wrong! Try again!')
    guess_counter += 1

# TODO: Explain to me what you think this program is doing?

# TODO: (Challenge) What do you think this program would do?

# while True:
#     print('Hello World!')





# while True loops are the only loops that do not have a variable that changes.

"""
One last thing about loops:
There is a keyword that is "break"
When python sees the "break" keyword, it will immediately go out of the loop
"""

# Example:

# while True:
#     user_input = input('Give me an input: ')
#     if user_input == 'STOP':
#         break
#     print('You are still in the loop')
# print('You have exited the loop!')

# The program above keeps asking the user for an input until the user types "STOP"
# When the user types "STOP", the program goes out of the loop.
# Try running it!

