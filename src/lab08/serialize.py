import json
from typing import List
from lab08.models import Student

def students_to_json(students: List[Student], path: str) -> None:
    data = [student.to_dict() for student in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)




def students_from_json(path: str) -> List[Student]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        students = [Student.from_dict(item) for item in data]
        return students
    except FileNotFoundError:
        print(f"Error: file not found")
        raise FileNotFoundError
    except json.JSONDecodeError:
        print(f"Error: bad encoding")
        raise json.JSONDecodeError
    except KeyError as e:
        print(f"Error: lacking field {e} in data")
        raise KeyError

#students_to_json(students_from_json('/home/kirill/Documents/VSC/python_labs/data/lab08/students_input.json'), '/home/kirill/Documents/VSC/python_labs/data/lab08/students_output.json')