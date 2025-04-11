# String Formatting and Basic String Operations

greeting = "Hello World!"

print(len(greeting)) # length of the string

print(greeting.split()) # split the string into a list of characters

print(greeting.upper()) # convert the string to uppercase

print(greeting.index("e")) # find the index of the first occurrence of "e"

print(greeting.count("l")) # count the number of occurrences of "l"

print(greeting.replace("World", "Python"))

print(greeting.lower()) # convert the string to lowercase

print(greeting[2:5]) # slice the string from index 2 to 5. It should print "llo"

print(greeting[2:5:2]) # slice the string from index 2 to 5 with a step of 2. It should print "l"

print(greeting[::-1]) # reverse the string. It should print "!dlroW olleH"

name = "Zora"
age = 23

print("Hello, my name is: " + name) # concatenating strings
print("%s is about to turn %d" % (name, age)) # using % operator for string formatting


