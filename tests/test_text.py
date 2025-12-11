# tests/test_text.py
import pytest
from lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы   ", "двойные пробелы"),
        ("", ""),
        ("!@#$%^&*()", "!@#$%^&*()"),
        ("  \t\n  ", ""),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello world!", ["hello", "world!"]),
        ("", []),
        ("   ", []),
        ("слово, слово. слово!", ["слово,", "слово.", "слово!"]),
        ("one1 two2", ["one1", "two2"]),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


def test_count_freq():
    tokens = ["a", "b", "a", "c", "b", "a"]
    expected = {"a": 3, "b": 2, "c": 1}
    assert count_freq(tokens) == expected
    assert count_freq([]) == {}


def test_top_n():
    freq = {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    assert top_n(freq, 5) == [("a", 3), ("b", 2), ("c", 1)]
    assert top_n({}, 1) == []


def test_top_n_tie_breaker():
    freq = {"яблоко": 2, "банан": 2, "вишня": 2}
    result = top_n(freq, 3)
    expected = [("банан", 2), ("вишня", 2), ("яблоко", 2)]
    assert result == expected
