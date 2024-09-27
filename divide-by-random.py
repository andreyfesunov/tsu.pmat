#!/usr/bin/python3

from sys import stderr, exit
from random import randint
from math import inf

def error_to_sdterr(msg):
    print(msg, file = stderr)
    exit(1)

def validate_float(data):
    if not data:
        error_to_sdterr("Error: No data provided")

    try:
        return float(data)
    except ValueError:
        error_to_sdterr("Error: Please, enter a number")

def divide_by_random(number):
    random = randint(-10, 10)
    if random == 0:
        return inf
    return number / random

print(divide_by_random(validate_float(input())))

