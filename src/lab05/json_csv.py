import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    if (csv_path[-4:]!='.csv'): raise ValueError('Inappropiate output file.') 
    try:
        with Path(json_path).open('r', encoding="utf-8") as f:
            temp = json.load(f)
    except:
        raise FileNotFoundError(f'No such .json file.')
    try: 
        with Path(csv_path).open('w', encoding="utf-8") as f:
            if not temp:
                raise ValueError("Empty JSON or unsupported structure")
            fieldnames = temp[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(temp)
    except:
        raise FileNotFoundError(f'No such .csv file.')

#json_to_csv(json_path='/home/kirill/Documents/VSC/python_labs/data/lab05/samples/people.json', csv_path='/home/kirill/Documents/VSC/python_labs/data/lab05/out/people_from_json.csv')
    
def csv_to_json(csv_path: str, json_path: str) -> None:
    if (json_path[-5:]!='.json'): raise ValueError('Inappropiate output file.') 
    try: 
        with Path(csv_path).open('r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            temp = []
            for row in reader:
                temp.append(row)
    except:
        raise FileNotFoundError(f'No such .csv file.')
    try:
        with Path(json_path).open('w', encoding="utf-8") as f:
            json.dump(temp, fp=f)
    except:
        raise FileNotFoundError(f'No such .json file.')


#csv_to_json(csv_path='/home/kirill/Documents/VSC/python_labs/data/lab05/samples/people.csv', json_path='/home/kirill/Documents/VSC/python_labs/data/lab05/out/people_from_csv_1.csv')

