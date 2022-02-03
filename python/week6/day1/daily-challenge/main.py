# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
#
# Then, print the first and last characters of the given text.
#
# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World
#
#
# 4. Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
#
# Hlrolelwod
import random

inputText = input("please write a 10 characters long string: ")
if len(inputText) < 10:
    print("not long enough")
if len(inputText) > 10:
    print("too long")
if len(inputText) == 10:
    # first and last
    print(inputText[0])
    print(inputText[9])
    # characters one by one
    for i in range(len(inputText)):
        print(inputText[0:i+1])
    inputList = list(inputText)
    random.shuffle(inputList)
    print("".join(inputList))

