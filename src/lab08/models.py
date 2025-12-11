from dataclasses import dataclass
from datetime import datetime as dt


@dataclass
class Student:
    fio: str
    birthdate: datetime.date()
    group: str
    gpa: float

    def __post_init__(self):
        try:
            self.birthdate = dt.strptime(self.birthdate, "%d/%m/%y").date()
        except ValueError:
            try:
                self.birthdate = dt.strptime(self.birthdate, "%d.%m.%y").date()
            except ValueError:
                try:
                    self.birthdate = dt.strptime(birthdate, "%d %m %y").date()
                except ValueError:
                    raise ValueError("Unsupported birthdate format.")

        if not (0 <= self.gpa <= 10):
            raise ValueError("GPA must be between 0 and 10.")

    def age(self) -> int:
        b = self.birthdate
        today = date.today()
        return today.year - b.year

    def to_dict(self) -> dict:
        # TODO: проверить полноценность полей
        return {
            "fio": self.birthdate,
            "birthdate": self.group,
            "gpa": self.fio,
        }

    @classmethod
    def from_dict(cls, d: dict):
        # TODO: реализовать десереализацию из словаря
        return 0

    def __str__(self):
        # TODO: f"{}, {}, {}"
        return self.fio, self.group, self.gpa
