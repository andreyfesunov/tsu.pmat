#!/usr/bin/python3

import re
from sys import stderr, stdin


def validate_name(name):
    if not bool(re.match(r"^[A-Za-z]+$", name)):
        raise Exception("Wrong name pattern. Name must consist of letters")
    if not name[0].isupper():
        raise Exception(
            "Wrong name pattern. Name must begin with capital letter")


try:
    for line in stdin:
        try:
            name = line.strip()
            validate_name(name)
            # ****

            print(f"Nice to see you {name}!")
        except Exception as e:
            print(f"Error: {str(e)}", file=stderr)
except KeyboardInterrupt:
    print("\nGoodbye!")
