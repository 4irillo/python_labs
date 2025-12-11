# Обзор кода для lab07
Начнем с тестов для либы ```text.py```
``` python 
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
```
Тесты генерировала нейросеть замечательная, часть я у Вас спер нагло, ничего примечательного тут нет абсолютно. Из особенного как оказывается я неправильно текст от пробелов чистил и один пробел таки оставался в конце, пришлось переписать функцию ```normalize```. Так же улучшил читабельность ```tokenize```

Далее идет тесты для lab05 aka ```json_csv formating```
``` python
import json
import csv
from pathlib import Path
import pytest
from lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert set(rows[0].keys()) == {"name", "age"}
    assert rows[0]["name"] == "Alice"
    assert rows[1]["age"] == "25"


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    rows = [
        {"name": "Charlie", "age": "30"},
        {"name": "Diana", "age": "28"},
    ]
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(rows)

    csv_to_json(str(src), str(dst))

    result = json.loads(dst.read_text(encoding="utf-8"))
    assert len(result) == 2
    assert result[0]["name"] == "Charlie"
    assert result[1]["age"] == "28"


def test_json_to_csv_empty_file(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "empty.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_empty_file(tmp_path: Path):
    src = tmp_path / "empty.csv"
    dst = tmp_path / "empty.json"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


def test_json_to_csv_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "out.csv")


def test_csv_to_json_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        csv_to_json("nonexistent.csv", "out.json")
```
Я честно не знаю что тут писать, тесты придумывала нейросеть, а не я, были проблемы c поднятием ошибок, пришлось все переделывать, чтобы ошибки кидались корректно.
# Валидный ран всех тестов лежит в папочке ```test_results``` в файле угадайте каком.