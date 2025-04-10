# Generator Function Called Count_Up_To

def count_up_to(n):
    count = 0
    while count <= n:
        print(f"The current count is: {count}")
        yield count # What yield does is it returns the value of count and pauses the function
        # until the next value is requested.
        count += 1 # Increment the count by 1

# Example usage of the generator function
n = 10
for number in count_up_to(n):
    print(number)