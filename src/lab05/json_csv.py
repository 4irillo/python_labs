import json
import csv
from openpyxl import Workbook
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    try:
        with Path(json_path).open('r', encoding="utf-8") as f:
            temp = json.load(f)
            if (not len(f)):
                raise ValueError("Пустой JSON или неподдерживаемая структура")
    except:
        raise FileNotFoundError(f'No such .json file.')
    try: 
        with Path(csv_path).open('w', encoding="utf-8") as f:
            csv.writer('name, age, city')
            csv.DictWriter(f, fieldnames=['name', 'age', 'city']).writerows(temp)
    except:
        raise FileNotFoundError(f'No such .csv file.')

#json_to_csv(json_path='/home/kirill/Documents/VScode/python_labs/data/lab05/samples/people.json', csv_path='/home/kirill/Documents/VScode/python_labs/data/lab05/out/people_from_json.csv')
    
def csv_to_json(csv_path: str, json_path: str) -> None:
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


#csv_to_json(csv_path='/home/kirill/Documents/VScode/python_labs/data/lab05/samples/people.csv', json_path='/home/kirill/Documents/VScode/python_labs/data/lab05/out/people_from_csv.json')

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    try: 
        with Path(csv_path).open('r', encoding="utf-8") as f:
            for row in csv.reader(f):
                ws.append(row)
            wb.save(xlsx_path)
    except: 
        raise FileNotFoundError(f'No such .csv file.')

csv_to_xlsx(csv_path='/home/kirill/Documents/VScode/python_labs/data/lab05/samples/people.csv', xlsx_path='/home/kirill/Documents/VScode/python_labs/data/lab05/out/people.xlsx')