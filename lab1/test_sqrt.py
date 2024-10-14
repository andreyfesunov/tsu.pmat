#!/usr/bin/python3

import pytest

import sqrt


def test_no_data(monkeypatch):
    input_data = ""
    monkeypatch.setattr("builtins.input", lambda: input_data)

    with pytest.raises(SystemExit):
        sqrt.main()


def test_invalid_data(monkeypatch):
    input_data = "test"
    monkeypatch.setattr("builtins.input", lambda: input_data)

    with pytest.raises(SystemExit):
        sqrt.main()


def test_negative_data(monkeypatch):
    input_data = -2
    monkeypatch.setattr("builtins.input", lambda: input_data)

    with pytest.raises(SystemExit):
        sqrt.main()


def test_ok(monkeypatch, capfd):
    input_data = 4
    monkeypatch.setattr("builtins.input", lambda: input_data)

    filename = "output-test.txt"
    sqrt.sqrt_from_stdin(filename)

    with open(filename, "r") as file:
        last_line = file.readlines()[-1]
        assert float(last_line) == 2.0
