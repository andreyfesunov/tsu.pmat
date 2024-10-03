#!/usr/bin/python3

from sys import stderr, exit
from random import randint
from math import inf


def validate_float(data):
    if not data:
        raise Exception("No data provided")

    try:
        return float(data)
    except ValueError:
        raise Exception("Enter a number")


def divide_by_random(number):
    random = randint(-10, 10)
    if random == 0:
        return inf
    return number / random


try:
    print(divide_by_random(validate_float(input())))
except Exception as e:
    print("Error: " + str(e), file=stderr)
    exit(1)
