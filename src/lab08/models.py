from dataclasses import dataclass
from datetime import datetime as dt, date
import json


@dataclass
class Student:
    fio: str
    birthdate: str 
    group: str
    gpa: float
    
    def __post_init__(self):
        original_birthdate = self.birthdate
        date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%d.%m.%Y", "%d %m %Y"]
        
        for date_format in date_formats:
            try:
                self._birthdate_obj = dt.strptime(self.birthdate, date_format).date()
                self.birthdate = self._birthdate_obj.isoformat()
                break
            except ValueError:
                continue
        else:
            raise ValueError(f"Unsupported birthdate format: '{original_birthdate}'. Expected formats: YYYY-MM-DD, DD/MM/YYYY, DD.MM.YYYY, DD MM YYYY")
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA must be between 0 and 5, got: {self.gpa}")
        if not self.group.strip():
            raise ValueError("Group cannot be empty")
    
    @property
    def birthdate_obj(self) -> date:
        if hasattr(self, '_birthdate_obj'):
            return self._birthdate_obj
        else:
            self._birthdate_obj = dt.strptime(self.birthdate, "%Y-%m-%d").date()
            return self._birthdate_obj
    
    def age(self) -> int:
        today = date.today()
        birth_date = self.birthdate_obj
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1   
        return age
    
    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        required_fields = ["fio", "birthdate", "group", "gpa"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"])
        )
    
    def __str__(self):
        return f"Student: {self.fio}, Group: {self.group}, GPA: {self.gpa:.2f}, Age: {self.age()}"
    
    def __repr__(self):
        return f"Student(fio='{self.fio}', birthdate='{self.birthdate}', group='{self.group}', gpa={self.gpa})"


if __name__ == "__main__":
    test_dates = ["2007-25-04", "25/04/2007", "25.04.2007", "25 04 2007", "14."]
    
    for test_date in test_dates:
        try:
            student = Student(
                fio="Aa Aa Aa",
                birthdate=test_date,
                group="SE-01",
                gpa=4.5
            )
            print(f"Successful initiation with birthdate '{test_date}': {student}")
            print(f"\tStandart {student.birthdate}")
            print(f"\tAge: {student.age()}")
            print(f"\tDictForm: {student.to_dict()}\n")
        except ValueError as e:
            print(f"Improper date: '{test_date}': {e}")
   
    test_dict = {
        "fio": "Aa Aa Aa",
        "birthdate": "2001-08-22",
        "group": "CS-02",
        "gpa": 4.8
    }
    
    try:
        student_from_dict = Student.from_dict(test_dict)
        print(f"Student {student_from_dict}")
    except ValueError as e:
        print(f"Initialization error {e}")