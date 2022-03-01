# exercise 1
import datetime
now = datetime.datetime.now()
print(now)

# exercise 2
# future_date = datetime.datetime(2023, 1, 1)
# print(f"time left is {future_date - now}")

# exercise 3
# birth_year = input("enter your birth year: ")
# birth_month = input("enter your birth month: ")
# birth_day = input("enter your birth day: ")
# birthdate = datetime.datetime(int(birth_year), int(birth_month), int(birth_day))
# time_alive = now - birthdate
# print(time_alive.total_seconds() / 60)

# exercise 4
# purim = datetime.datetime(2022, 3, 16)

# def time_until_purim():
#     print(f"todays date is {now}")
#     print(f"time until purim is {purim - now}")

# time_until_purim()

# exercise 5
# age_seconds = input("how old are you in seconds?: ")
# print(f"earth age is {int(age_seconds) / 31557600}")
# print(f"mercury age is {int(age_seconds) / (31557600 * 0.2408467)}")
# print(f"venus age is {int(age_seconds) / (31557600 * 0.61519726)}")
# print(f"mars age is {int(age_seconds) / (31557600 * 1.8808158)}")
# print(f"jupiter age is {int(age_seconds) / (31557600 * 11.862615)}")
# print(f"saturn age is {int(age_seconds) / (31557600 * 29.447498)}")
# print(f"uranus age is {int(age_seconds) / (31557600 * 84.016846)}")
# print(f"neptune age is {int(age_seconds) / (31557600 * 164.79132)}")

# exercise 6 
from faker import Faker
fake = Faker()
print(fake.name())

users = []

def add_new():
    users.append({'Name': fake.name(), 'Address': fake.address(), 'Language_code': fake.language_code()})

add_new()
print(users)