#!/usr/bin/python3

import re
from sys import stderr, stdin


def validate_name(name: str):
    if not bool(re.match(r"^[A-Za-z]+$", name)):
        raise Exception("Wrong name pattern. Name must consist of letters")
    if not name[0].isupper():
        raise Exception("Wrong name pattern. Name must begin with capital letter")


def greet_names(names: list[str]):
    for name in names:
        try:
            validate_name(name)
            print(f"Nice to see you {name}!")
        except Exception as e:
            print(f"Error: {str(e)}", file=stderr)


def main():
    try:
        names = [line.strip() for line in stdin]
        greet_names(names)
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
