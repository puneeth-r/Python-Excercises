"""Sample program to illustrate list comprehensions in Python.
The below program takes the list [values] as input and prints the squares of each of
the value if it is divisible by 2"""
values = [2, 4, 6, 8, 10, 11]
numbers = [x ** 2 for x in values if x % 2 == 0]
print(numbers)
