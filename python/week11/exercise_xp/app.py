# exercise 1
# Write a program which prints the results of the following 
# python built-in functions: abs(), int(), input().

# def what_is_abs():
#     print(abs.__doc__)

# what_is_abs()

# def what_is_int():
#     print(int.__doc__)

# what_is_int()

# def what_is_input():
#     print(input.__doc__)

# what_is_input()

# # Using the __doc__ dunder method create your own documentation 
# # which explains the execution of your code. Take a look at the doc method on google for help.
# def say_hello(name):
#     """this function says hello"""
#     print(f'hello {name}')

# say_hello("maor")
# print(say_hello.__doc__)

# exercise 2
# Create the code which will output the results below.
# Hint : When adding 2 currencies which 
# don’t share the same label you should raise an error.

from locale import currency


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
       return f'{self.amount} {self.currency}s'

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f'{self.amount} {self.currency}s'

    def __add__(self, num):
        if type(num) == int:
            temp = Currency(self.currency, self.amount + int(num))
            return temp
        else:
            if self.currency == num.currency:
                temp = Currency(self.currency, self.amount + int(num))
                return temp
            else:
                print(f"TypeError cannot add between {self.currency} and {num.currency}")

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
c1 + c3