from functools import reduce
# This script demonstrates the use of map, filter, and reduce functions in Python.

numbers = [1,2,3,4,5,6,7,8,9,10]

squared = list(map(lambda x: x**2, numbers))
print(squared)

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

even_only = list(filter(lambda x: x % 2 == 0, numbers))
print(even_only)

total = reduce(lambda x, y: x + y, numbers)
print(total)