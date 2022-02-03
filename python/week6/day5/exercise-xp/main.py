#  Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = zip(keys, values)
print(list(result))

# Exercise 2 : Cinemax #2
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_price = 0
for name in family:
    if family[name] < 3:
      print(f'for {name} the price is 0$') 
    if family[name] <= 12:
        print(f'for {name} the price is 10$') 
        total_price += 10
    if family[name] > 12:
        print(f'for {name} the price is 15$') 
        total_price += 15

print(f'the total price is {total_price}')

# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand = {
    "name": "zara",
    "creation_date": "1975",
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 3. Change the number of stores to 2.
brand["number_stores"] = 2

# 4. Print a sentence that explains who Zaras clients are.
print(f'zaras clients are {brand["type_of_clothes"][0]} {brand["type_of_clothes"][1]} {brand["type_of_clothes"][2]} and {brand["type_of_clothes"][3]} owners')

# 5. Add a key called country_creation with a value of Spain.
brand.update({"country_creation": "spain"})
print(brand)

# 6. Check if the key international_competitors is in the dictionary.
print(brand["international_competitors"])

# 7. Delete the information about the date of creation.
brand.pop("creation_date")
print(brand)

# 8. Print the last international competitor.
print(brand["international_competitors"][-1])

# 9. Print the major clothes colors in the US.
print(brand["major_color"]["US"])

# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))

# 11. Print the keys of the dictionary.
for key in brand:
    print(key)

# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)
print(brand)
# # the number stores got replaced

# Exercise 4 : Disney Characters
# Instructions
# Use this list :
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# Analyse these results :
# #1/
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# #2/
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# #3/ 
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
first_result = {}
for index,user in enumerate(users):
    first_result.update({user:index})
print(first_result)

# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
second_result = {}
for i in range(0,5):
    if i == 4:
        second_result.update({i:users[i]})
        break
    second_result.update({users[i]:i})
print(second_result)


# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
third_result = {}
users.sort()
for index,user in enumerate(users):
    third_result.update({user:index})
print(third_result)
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
first_result = {}
for index,user in enumerate(users):
    if "i" in user:
        first_result.update({user:index})
print(first_result)

# The characters, which names start with the letter “m” or “p”.
first_result = {}
for index,user in enumerate(users):
    if user[0] == "M" or user[0] == "P":
        first_result.update({user:index})
print(first_result)