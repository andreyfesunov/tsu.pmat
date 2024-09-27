#!/usr/bin/python3

from sys import stderr
from math import sqrt 

def error_to_sdterr(msg):
    print(msg, file = stderr)
    exit(1)

user_input = input()

if not user_input:
    error_to_sdterr("Error: No data provided")

number = None

try:
    number = float(user_input)
except ValueError:
    error_to_sdterr("Error: Please, enter a number")

# I'd like to get rid of that check but LSP marks that number can be unbound :(

if number is not None:
    if number < 0:
        error_to_sdterr("Error: Can't take the sqrt of a negative number")

    with open("output.txt", "a") as f:
        print(sqrt(number), file=f)
else:
    error_to_sdterr("Unhandled behaviour: Number is not defined")
