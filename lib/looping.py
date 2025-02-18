#!/usr/bin/env python3

# outputs numbers starting at 10 and counting down to 1
def happy_new_year():
    i=10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    # pass

# use list comprehension
# function takes in list of integers and returns list of squared elements
def square_integers(int_list):
    int_list = [(num * num) for num in int_list]
    return int_list
    # pass

# prints numbers 1 to 100
# for multiples of 3, print "Fizz"
# for multiples of 5, print "Buzz"
# for multiples of 3 and 5, print "FizzBuzz"
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    # pass
