# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling 
# everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message():
    print("i am learning about functions in python")

display_message()


# Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as 
# “One of my favorite books is Alice in Wonderland”.
# Call the function, make sure to include a book title as an 
# argument when calling the function.

def favorite_book(title):
    print(f'one of my favorite books is {title}')

favorite_book("alice in wonderland")

# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the 
# name of a city and its country as parameters.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the country parameter a default value.
# Call your function.

def describe_city(name,country="israel"):
    print(f'the city {name} is in the country {country}')

describe_city("tel aviv")
describe_city("shanghai","china")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 
# and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, 
# display a success message, otherwise show a fail message and display both numbers.

import random

def guess_number(user_guess):
    if int(user_guess) < 1 or int(user_guess) > 100:
        print("please choose a number between 1-100")
        return
    else:
        random_num = random.randrange(1, 100)
        if int(user_guess) == random_num:
            print("you guessed correctly!")
        else:
            print(f'you were wrong, you guessed {user_guess} but the answer is {random_num}')

user_input = input("choose a number 1-100: ")
guess_number(user_input)

# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text 
# of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt 
# and the message printed on it.
def make_shirt(size,text):
    print(f'the size is {size} and the message is {text}')

# Call the function make_shirt() using positional arguments to make a shirt.
make_shirt("small","i hate javascript")

# Modify the make_shirt() function so that shirts are large by default with 
# a message that reads I love Python.
def make_shirt2(size="large",text="i love pyton"):
    print(f'the size is {size} and the message is {text}')

# Make a large shirt and a medium shirt with the default message, and a shirt 
# of any size with a different message.
make_shirt2()
make_shirt2("medium")
make_shirt2("small", "i love c")


# Bonus: Call the function make_shirt() using keyword arguments.
make_shirt2(size="XXL",text="i love react")

# Exercise 6 : Magicians …
# Instructions
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), 
# which prints the name of each magician in the list.

magicians_names = ["amir", "nadav", "tomer", "ido"]

def show_magicians(names):
    for name in names:
        print(name)

show_magicians(magicians_names)

# Write a function called make_great() that modifies the list of magicians 
# by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the funcyion show_magicians() to see that the list has actually been modified.

def make_great(names):
    for index,name in enumerate(names):
        names[index] += " the great"

make_great(magicians_names)
show_magicians(magicians_names)