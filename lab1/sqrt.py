#!/usr/bin/python3

from sys import stderr
from math import sqrt


def main():
    user_input = input()

    if not user_input:
        raise Exception("No data provided")

    try:
        number = float(user_input)
    except ValueError:
        raise Exception("Enter a number")

    if number < 0:
        raise Exception("Can't take the sqrt of a negative number")

    with open("output.txt", "a") as f:
        print(sqrt(number), file=f)


try:
    main()
except Exception as e:
    print("Error: " + str(e), file=stderr)
    exit(1)
