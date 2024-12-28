"""
Goal: Format a phone number into (xxx) xxx-xxx

Description:
 - Ask the user for a 10 digit phone number (i.e. "1234567890").
 - Format it into (xxx) xxx-xxx format (i.e. "(123) 456-7890")

Examples:
 - The phone number "5103374285" would be formatted into "(510) 337-4285"
 - The phone number "9161066839" would be formatted into "(916) 106-6839"

Skills you probably will use:
 - Slicing
 - Concatenation

Feel free to ask if you are stuck or need hints!
"""
# Write code down here:

# The input is already done for you
# 1234567890
s = input('Enter a phone number: ')
x = s[0:3]
y = s[3:6]
z = s[6:]
print('(' + x + ') ' + y + '-' + z )

# '(abc) xyz-lmn'
