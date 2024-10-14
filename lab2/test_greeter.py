#!/usr/bin/python3

import greeter
import pytest


def test_numbers_in_name():
    with pytest.raises(Exception):
        greeter.validate_name("123Vlad")


def test_bad_symbols_in_name():
    with pytest.raises(Exception):
        greeter.validate_name("O'Neel")


def test_small_character():
    with pytest.raises(Exception):
        greeter.validate_name("max")


def test_ok():
    greeter.validate_name("Vlad")


def test_greet_names(capsys):
    greeter.greet_names(["Alice", "Bob"])
    captured = capsys.readouterr()
    assert "Nice to see you Alice!" in captured.out
    assert "Nice to see you Bob!" in captured.out


def test_greet_names_invalid(capsys):
    greeter.greet_names(["alice", "Bob123"])
    captured = capsys.readouterr()
    assert captured.out == ""
