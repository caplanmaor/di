# Exercise 1 : Hello World
print("hello world\n" * 4)

# Exercise 2 : Some Math Write code that calculates the result of: (99^3) * 8 (99 to the power of 3 times 8)
print(99**3)

# Exercise 3 : What Is The Output ? Predict the output of the following code snippets:
# 5 < 3
# false

# 3 == 3
# true

# 3 == "3"
# false

# "3" > 3
# invalid

# "Hello" == "hello"
# false

# Exercise 4 : Your Computer Brand
# 1 Create a variable called computer_brand which value is the brand name of your computer.
computer_brand = "dell"
# 2 Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
print(f"i have a {computer_brand} computer")

# Exercise 5 : Your Information
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = "maor"
age = 26
shoe_size = 43
info = "hi my name is " + str(name) + " im " + str(age) + " years old and my shoe size is " + str(shoe_size)
print(info)

# Exercise 6 : A & B
# Create two variables, a and b.
# Each variables value should be a number.
# If a is bigger then b, have your code print Hello World.
a = 6
b = 2
if a > b:
    print("hello world")

# Exercise 7 : Odd Or Even Write code that asks the user for a number and determines whether this number is odd or even.
input = int(input("give me a number: "))
if (input % 2) == 0:
    print(f"the number {input} is even")
else:
    print(f"the number {input} is odd")

# Exercise 8 : What’s Your Name ?
# Write code that asks the user for their name
# and determines whether or not you have the same name, print out a funny message based on the outcome.
name = "maor"
user_name = input("whats your name?: ")
if user_name == name:
    print("omg we have the same name")
else:
    print("we dont have the same name")

# Exercise 9 : Tall Enough To Ride A Roller Coaster
# Instructions
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.
height = int(input("whats your height in inches?: "))
height *= 2.54
if height > 145:
    print("you are tall enough to ride")
else:
    print("you need to grow some more to ride")