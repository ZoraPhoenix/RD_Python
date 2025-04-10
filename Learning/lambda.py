a = 10
b = 20
c = 30
sum = lambda x,y,z: x + y + z # Inline function used to add three numbers.
print(sum(a, b, c))

number_list = [1,2,3,4,5,6,7,8,9,10]

# lambda function to find if number is odd
for i in number_list:
    odd = lambda x: x % 2 != 0
    print(f"{i} is odd: {odd(i)}")