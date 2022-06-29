#!/usr/bin/env python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0:
            print("Fizz", end="")
        elif number % 5 == 0:
            print("buzz", end="")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end="")
        else:
            print("{} ".format(number, end=""))     
