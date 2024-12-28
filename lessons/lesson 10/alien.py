"""
Description:
 - In a land far, far away, there is a language where the vowels (a, e, i, o, u) are replaced with z's and space are replaced with dashes (-)
 - You must translate from English to that language

Examples:
 - If the user inputs "Hello World", you would print out "Hzllz-Wzrld"
 - If the user inputs "i like to drink juice", you would print out "z-lzkz-tz-drznk-jzzcz"

You will need to use:
 - The .replace() method
"""

s = input('Enter some english: ')
s = s.replace('a', 'z')
s = s.replace('e', 'z')
s = s.replace('i', 'z')
s = s.replace('o', 'z')
s = s.replace('u', 'z')
s = s.replace(' ', '-')
print(s)