'''
Write a python program using reduce function to compute the product of a list containing
numbers from 1 to 25.
'''

from functools import reduce

numbers = list(range(1, 26))
multiply = lambda x, y: x * y
product = reduce(multiply, numbers)
print("Product of numbers from 1 to 25:", product)
