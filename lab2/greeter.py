#!/usr/bin/python3

import re
from sys import stderr, stdin


def validate_name(name: str) -> None:
    if not bool(re.match(r"^[A-Za-z]+$", name)):
        raise Exception("Wrong name pattern. Name must consist of letters")
    if not name[0].isupper():
        raise Exception("Wrong name pattern. Name must begin with capital letter")


def greet_name(name: str) -> None:
    try:
        validate_name(name)
        print(f"Nice to see you {name}!")
    except Exception as e:
        print(f"Error: {str(e)}", file=stderr)


def tty_greeter() -> None:
    while True:
        print("Hey, what's your name?")
        greet_name(stdin.readline().strip())


def pipeline_greeter() -> None:
    for line in stdin:
        greet_name(line.strip())


def main() -> None:
    try:
        if stdin.isatty():
            tty_greeter()
        else:
            pipeline_greeter()
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
