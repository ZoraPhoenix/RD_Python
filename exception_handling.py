def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: 
            print("Index out of range!")

catch_this()
# The above code demonstrates exception handling in Python.
# It attempts to access elements in a list and catches an IndexError if the index is out of range.
# The try-except block allows the program to continue running even if an error occurs.