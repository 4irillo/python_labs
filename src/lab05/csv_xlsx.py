import csv
from openpyxl import Workbook
from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    if xlsx_path[-5:] != ('.xlsx' or '.xlsm' or '.xltx' or '.xltm'):
        raise ValueError('Inappropiate output file.')
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    try:
        with Path(csv_path).open('r', encoding="utf-8") as f:
            for row in csv.reader(f):
                ws.append(row)
            wb.save(xlsx_path)
    except:
        raise FileNotFoundError(f'No such .{xlsx_path[-5:]} file.')


# csv_to_xlsx(csv_path='/home/kirill/Documents/VSC/python_labs/data/lab05/samples/people.csv', xlsx_path='/home/kirill/Documents/VSC/python_labs/data/lab05/out/people.xlsx')
