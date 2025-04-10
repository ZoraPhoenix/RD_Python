def foo(first, second, third, fourth, *therest):
    print("first = ", first)
    print("second = ", second)
    print("third = ", third)
    print("fourth = ", fourth)
    print("The rest: ", therest) 

foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)