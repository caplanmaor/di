# exercise 1
from function import display_message as fn

# exercise 2
# from random import randrange
# random_number = randrange(100)
# user_input = input("choose a random number 1-100: ")
# if random_number == user_input:
#     print(f"you chose the right number {random_number}")
# else:
#     print(f"wrong the number was {random_number}")

# exercise 3
import string
import random
letters = string.ascii_letters
random_string = " "
for i in range(10):
    random_string += random.choice(letters)

print(random_string)

