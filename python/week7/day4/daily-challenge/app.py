try:
    (lambda x: 5 / x)(0)
except ZeroDivisionError:
    print("you cant divide by zero")