# ЛАБА 05  
Конвертим JSON ↔ CSV ↔ XLSX  
# Первое задание
``` python
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

```
Я не знаю что тут надо писать, закинул экспешены на пустые файлы, если read файл не находится, библиотека сама ругается, если out файл не находится, он создается, мне кажется удобно


# Второе задание
``` python
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    if (xlsx_path[-5:]!=('.xlsx' or '.xlsm' or '.xltx' or '.xltm')): raise ValueError('Inappropiate output file.') 
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
```
Супер тупо, супер напрямую, но функционирует. Главное — не подсовывать пустые файлы или мусор :)  

# Как с этим работать?
``` python
#до этого импортим сами библиотеки очев
json_csv.json_to_csv('samples/people.json', 'out/people.csv')
json_csv.csv_to_json('samples/people.csv', 'out/people.json')
csv_xlsx.csv_to_xlsx('samples/people.csv', 'out/people.xlsx')
```
Все работает отлично, сам тестил 
