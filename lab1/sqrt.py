#!/usr/bin/python3

from math import sqrt
from sys import stderr


def sqrt_from_stdin(filename):
    user_input = input()

    if not user_input:
        raise Exception("No data provided")

    try:
        number = float(user_input)
    except ValueError:
        raise Exception("Enter a number")

    if number < 0:
        raise Exception("Can't take the sqrt of a negative number")

    with open(filename, "a") as f:
        print(sqrt(number), file=f)


def main():
    try:
        sqrt_from_stdin("output.txt")
    except Exception as e:
        print("Error: " + str(e), file=stderr)
        exit(1)


if __name__ == "__main__":
    main()
