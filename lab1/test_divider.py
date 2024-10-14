#!/usr/bin/python3

from math import inf

import pytest

import divider

# UNIT TESTS


def test_divide_ok():
    result = divider.divide(10, 5)
    assert result == 2


def test_divide_inf():
    result = divider.divide(10, 0)
    assert result == inf


def test_input_data_no_data():
    with pytest.raises(Exception):
        divider.validate_float("")


def test_input_data_invalid():
    with pytest.raises(Exception):
        divider.validate_float("test")


def test_input_data_ok():
    assert 2.0 == divider.validate_float("2")


# STDIN TESTS


def test_ok(monkeypatch, capfd):
    input_data = 2
    monkeypatch.setattr("builtins.input", lambda: input_data)

    divider.main()
    out, err = capfd.readouterr()

    assert err == ""


def test_no_input(monkeypatch):
    input_data = ""
    monkeypatch.setattr("builtins.input", lambda: input_data)

    with pytest.raises(SystemExit):
        divider.main()


def test_invalid_data(monkeypatch):
    input_data = "test"
    monkeypatch.setattr("builtins.input", lambda: input_data)

    with pytest.raises(SystemExit):
        divider.main()
