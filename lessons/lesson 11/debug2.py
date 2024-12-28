# The following program is a password critiquer. It's supposed to check how strong the password is.

# However, there are 5 bugs in this program! Try to find all of them and fix the program!

password = input('Enter a password: ')

if len(password) < 5:
    print('This is a weak password')
elif len(password) < 10:
    print('This is an ok password')
else:
    print('This is a very strong password')