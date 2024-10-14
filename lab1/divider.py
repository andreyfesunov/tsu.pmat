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


def divide(numerator, denominator):
    if denominator == 0:
        return inf
    return numerator / denominator


def main():
    try:
        random = randint(-10, 10)
        print(divide(validate_float(input()), random))
    except Exception as e:
        print("Error: " + str(e), file=stderr)
        exit(1)


if __name__ == "__main__":
    main()
