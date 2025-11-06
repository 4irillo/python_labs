from csv import writer
import sys
import os
import pathlib
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def read_text(path: str | pathlib.Path, encoding: str = "utf-8") -> str:
    try:
        with open(path, 'r', encoding=encoding) as file:
            content = file.read()
    except:
        raise FileNotFoundError('No such file or directory')
    return content

def write_csv(rows: list[tuple | list], path: str | pathlib.Path, header: tuple[str, ...] | None = None) -> None:
    try:
        with open(path, 'w', newline="") as file:
            w= writer(file)
            if (header != None): w.writerows(header)
            w.writerows(rows)
    except:
        raise FileNotFoundError("No such file or directory")
