import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    if not json_path.lower().endswith('.json'):
        raise ValueError('Inappropriate input file. Expected .json extension.')
    if not csv_path.lower().endswith('.csv'):
        raise ValueError('Inappropriate output file. Expected .csv extension.')
    try:
        with Path(json_path).open('r', encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                raise ValueError('Empty JSON file.')
            temp = json.loads(content)
    except FileNotFoundError:
        raise FileNotFoundError(f'No such .json file.')
    except json.JSONDecodeError:
        raise ValueError('Invalid JSON format.')
    if not isinstance(temp, list):
        raise ValueError('JSON must be a list.')
    if not temp:
        raise ValueError('Empty JSON data.')
    try:
        with Path(csv_path).open('w', encoding="utf-8", newline='') as f:
            fieldnames = temp[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(temp)
    except FileNotFoundError:
        raise FileNotFoundError(f'No such .csv file.')


# json_to_csv(json_path='/home/kirill/Documents/VSC/python_labs/data/lab05/samples/people.json', csv_path='/home/kirill/Documents/VSC/python_labs/data/lab05/out/people_from_json.csv')


def csv_to_json(csv_path: str, json_path: str) -> None:
    if not csv_path.lower().endswith('.csv'):
        raise ValueError('Inappropriate input file. Expected .csv extension.')
    if not json_path.lower().endswith('.json'):
        raise ValueError('Inappropriate output file. Expected .json extension.')
    try:
        with Path(csv_path).open('r', encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                raise ValueError('Empty CSV file.')
        with Path(csv_path).open('r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if not rows:
                raise ValueError('CSV file has no data rows.')
    except FileNotFoundError:
        raise FileNotFoundError(f'No such .csv file.')
    try:
        with Path(json_path).open('w', encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        raise FileNotFoundError(f'No such .json file.')


# csv_to_json(csv_path='/home/kirill/Documents/VSC/python_labs/data/lab05/samples/people.csv', json_path='/home/kirill/Documents/VSC/python_labs/data/lab05/out/people_from_csv_1.csv')
