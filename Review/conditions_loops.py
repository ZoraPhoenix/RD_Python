# Module for practicing conditions and loops in Python

x = 5
print(x == 2)  # False
print (x == 5)  # True
print (x < 10)  # True
print (x > 10)  # False

if x == 5:
    print("It is true that x = 5")
else:
    print("It is false that x = 5")

name = "Bob"
if name in ["Alice", "Bob"]: # Check if name is in the list
    print("Hello, Alice or Bob!")

# The is operator checks if two variables point to the same object in memory
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # False, because they are two separate instances.
# The not operator negates a boolean value
print(not True) # False
print(not False) # True


# For Loop
primes = [2,3,5,7,11,13,17,19,23,29]
for prime in primes:
    print(prime, end=" ")  # Prints all primes on the same line

for x in range(5):
    print(x, end=" ")  # Prints numbers from 0 to 4 on the same line

for x in range(5, 10):
    print(x) # Prints numbers from 5 to 9 on separate lines

# While Loop
count = 0
while count < 10:
    print(count, end=" ") # Prints numbers from 0 to 9 on the same line
    count += 1

second_count = 0
while True:
    print(count)
    count += 1
    if count >= 10:
        break # Breaks out of the loop when count is 10 or more

# Prints out only odd numbers
for x in range(10):
    if x % 2 == 0:
        continue # Skips the even numbers
    print(x, end=" ") # Prints odd numbers from 0 to 9 on the same line