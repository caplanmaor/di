# Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
# 


fav_num = {1,2,3,4}


fav_num.add(5)

fav_num.add(6)
print(fav_num)

friend_fav_num = {7,8,9}
our_fav_numbers = fav_num.union(friend_fav_num)
print(our_fav_numbers)

# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# answer: no tuples in Python are immutable, so you cannot append variables to a tuple once it is created.

# Exercise 3: Print A Range Of Numbers
# Use a for loop to print all numbers from 1 to 20, inclusive.

for i in range(20):
	print(i+1)

# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# a float has a decimal point and an int does not

sequence = []
for i in range(3,11):
	sequence.append(float(i / 2))
print(sequence)

# Exercise 5: Shopping List
# Instructions
# Using this list 
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
# Remove “Banana” from the list.
basket.remove("Banana")
print(basket)
# Remove “Blueberries” from the list.
basket.remove("Blueberries")
print(basket)
# Add “Kiwi” to the end of the list.
basket.append("Kiwi")
print(basket)
# Add “Apples” to the beginning of the list.
basket.insert(0,"Apples")
print(basket)
# Count how many apples are in the basket.
count = 0
for i in basket:
	if i == "Apples":
		count += 1

print(f'there are {count} apples in the basket')
# Empty the basket.
basket = []
# Print(basket)
print(basket)

# Exercise 6 : Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
myName = "maor"
userName = ""
# while userName != myName:
# 	userName = input("whats your name?: ")

# Exercise 7
# Instructions
# Given a list, use a loop to print out every element which has an even index.
fruits = ["apple", "banana", "melon", "mango"]
for index,item in enumerate(fruits):
	if (index%2) == 0:
		print(item)


# Exercise 8
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for i in range(1500,2000):
	if i%5 == 0 and i%7 == 0:
		print(i)

# Exercise 9: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
# userFruits = input("write your favorite fruits separated by space: ")
# fruitsList = list(userFruits.split(" "))
# checkFruit = input("name a fruit: ")
# isFavorite = False
# for i in fruitsList:
# 	if checkFruit == i:
# 		isFavorite = True

# if isFavorite:
# 	print("you chose your favorite fruit")
# else:
# 	print("you chose a new fruit")

# Exercise 10: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings = []
userInput = ""
# while userInput != "quit":
# 	userInput = input("choose toppings: ")
# 	if userInput != "quit":
# 		toppings.append(userInput)
# 		print("topping added")
# print(f'{toppings} total prize is {10 + (2.5 * len(toppings))}')

# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.

# ages = input("write your ages separated by space: ")
# agesList = list(ages.split(" "))
# total = 0
# canWatch = []
# for i in agesList:
# 	if int(i) < 3:
# 		print(f'for {i} the ticket is free')
# 	elif int(i) <= 12:
# 		print(f'for {i} the ticket is 10$')
# 		total += 10
# 	elif int(i) < 16:
# 		print(f'for {i} the ticket is 15$')
# 		total += 15
# 	elif int(i) >= 16:
# 		print(f'for {i} the ticket is 15$')
# 		total += 15
# 		canWatch.append(i)

# print(f'the total is {total} but only {canWatch} can watch the movie')

# Exercise 12 : Who Is Under 16?
# Instructions
# Given a list of names, write a program that asks every user for their age, if they are less than 16 years old remove them from the list.
# At the end, print the final list.

listNames = ["noam", "daniel", "yotam"]
print(listNames)
namesToRemove = []
for name in listNames:
	age = input(f'what is the age of {name}?: ')
	if int(age) < 16:
		namesToRemove.append(name)

for name in namesToRemove:
	listNames.remove(name)

print(listNames)

# Exercise 13
# Instructions
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = ["bagel", "grilled cheese", "hamburger"]
finished_sandwiches = []

for item in sandwich_orders:
	finished_sandwiches.append(item)

for item in sandwich_orders:
	print(f'i made your {item} sandwich')

# Exercise 14
# Instructions
# Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
sandwich_orders = ["pastrami", "bagel", "pastrami", "grilled cheese", "pastrami", "hamburger"]
print("out of pastrami")
toDelete = []

i = len(sandwich_orders)
while i > 0:
	if sandwich_orders[i] == "pastrami":
		toDelete.append(sandwich_orders[i])
	i -= 1

j = len(toDelete)
while j > 0:
	sandwich_orders.remove(toDelete[j])
