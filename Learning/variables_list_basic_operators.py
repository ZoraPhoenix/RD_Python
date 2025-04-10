# This is a simple Python script that demonstrates the use of variables, lists, and basic operators.

def adding_numbers(a, b):
    return a + b

names = ["Zora", "Sonic", "Tails", "Knuckles"] # list of names

numbers = [1, 2, 3, 4, 5] # list of numbers

index_zero = numbers[0] 
print(index_zero)

index_sonic = names[1] # accessing the second element of the list
print(index_sonic)

names[0] = "Shadow" # reassigning the first element of the list
print(names)

first_name = "Zora"
last_name = "Phoenix"

print(first_name + " " + last_name) # concatenating strings

print(f"{names[1]} is the name of a character from the Sonic The Hedgehog Series.") # f-string

a,b = 1,2 # tuple unpacking is a way to assign multiple variables at once
print(a,b)

names.append("Amy") # adding a new name to the list
print(names)

arithmetic = 1 + 9 * 2 / 2 - 1 # arithmetic operations
print(arithmetic)