#!/usr/bin/python3

from math import inf
from random import randint
from sys import exit, stderr


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


def main():
    try:
        print(divide_by_random(validate_float(input())))
    except Exception as e:
        print("Error: " + str(e), file=stderr)
        exit(1)


if __name__ == "__main__":
    main()
