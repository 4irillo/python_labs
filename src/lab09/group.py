import csv
import json
from pathlib import Path
from typing import List, Dict, Any
from lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)

    def _read_all(self) -> List[Dict[str, Any]]:
        if not self.path.exists():
            return []
        
        students_data = []
        with open(self.path, 'r', encoding='utf-8') as f:
            try:
                reader = csv.DictReader(f)
                for row in reader:
                    if not row:
                        continue
                    students_data.append({
                        "fio": row.get("fio", "").strip(),
                        "birthdate": row.get("birthdate", "").strip(),
                        "group": row.get("group", "").strip(),
                        "gpa": float(row.get("gpa", 0)) if row.get("gpa") else 0.0
                    })
            except Exception as e:
                print(f"Warning: error reading CSV file: {e}")
        
        return students_data

    def list(self) -> List[Student]:
        students = []
        for data in self._read_all():
            try:
                student = Student.from_dict(data)
                students.append(student)
            except Exception as e:
                print(f"Warning: skipping invalid student data {data}: {e}")
        return students

    def add(self, student: Student) -> bool:
        try:
            file_exists = self.path.exists()
            
            with open(self.path, 'a', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
                if not file_exists:
                    writer.writeheader()
                writer.writerow(student.to_dict())
            return True
            
        except Exception as e:
            print(f"Error: unable to add student: {e}")
            return False

    def find(self, substr: str) -> List[Student]:
        all_students = self.list()
        substr_lower = substr.lower()
        return [student for student in all_students if substr_lower in student.fio.lower()]

    def remove(self, fio: str) -> bool:
        try:
            students_data = self._read_all()
            if not students_data:
                return False
                
            filtered_data = [data for data in students_data if data["fio"].lower() != fio.lower()]
            
            if len(filtered_data) == len(students_data):
                return False
                
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
                writer.writeheader()
                writer.writerows(filtered_data)
            return True
            
        except Exception as e:
            print(f"Error: unable to remove student: {e}")
            return False

    def update(self, fio: str, **fields) -> bool:
        try:
            students_data = self._read_all()
            updated = False
            
            for data in students_data:
                if data["fio"].lower() == fio.lower():
                    for field, value in fields.items():
                        if field in data:
                            data[field] = value
                    updated = True
                    
            if not updated:
                return False
                
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
                writer.writeheader()
                writer.writerows(students_data)
            return True
            
        except Exception as e:
            print(f"Error: unable to update student: {e}")
            return False

    def stats(self) -> Dict[str, Any]:
        all_students = self.list()
        
        if not all_students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5_students": []
            }
        
        gpa_values = [student.gpa for student in all_students]
        groups_stats = {}
        
        for student in all_students:
            group = student.group
            groups_stats[group] = groups_stats.get(group, 0) + 1
        
        sorted_students = sorted(all_students, key=lambda s: s.gpa, reverse=True)
        top_5 = [{"fio": student.fio, "gpa": student.gpa} for student in sorted_students[:5]]
        
        return {
            "count": len(all_students),
            "min_gpa": min(gpa_values),
            "max_gpa": max(gpa_values),
            "avg_gpa": sum(gpa_values) / len(gpa_values),
            "groups": groups_stats,
            "top_5_students": top_5
        }

    def export_to_json(self, json_path: str) -> bool:
        try:
            students = self.list()
            students_dicts = [student.to_dict() for student in students]
            
            json_path_obj = Path(json_path)
            json_path_obj.parent.mkdir(parents=True, exist_ok=True)
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(students_dicts, f, ensure_ascii=False, indent=2)
            return True
            
        except Exception as e:
            print(f"Error: cannot export to JSON: {e}")
            return False


if __name__ == "__main__":
    print("=== Testing Group class ===")
    
    db_path = "data/lab09/students.csv"
    group = create_sample_database(db_path)
    
    print(f"\n1. File path: {group.path.absolute()}")
    
    print("\n2. All students in database:")
    students = group.list()
    for i, student in enumerate(students, 1):
        print(f"   {i}. {student}")
    
    print("\n3. Searching for students with 'Иван':")
    found = group.find("Иван")
    for student in found:
        print(f"   - {student}")
    
    print("\n4. Adding new student:")
    new_student = Student("Новиков Сергей Александрович", "2002-01-20", "БИВТ-21-4", 4.0)
    if group.add(new_student):
        print(f"   Added: {new_student}")
    
    print("\n5. Updating GPA for 'Иванов Иван Иванович':")
    if group.update("Иванов Иван Иванович", gpa=4.8):
        print("   GPA updated successfully")
    
    print("\n6. Group statistics:")
    stats = group.stats()
    print(f"   Total students: {stats['count']}")
    print(f"   Average GPA: {stats['avg_gpa']:.2f}")
    print(f"   Min GPA: {stats['min_gpa']}")
    print(f"   Max GPA: {stats['max_gpa']}")
    print(f"   Groups distribution: {stats['groups']}")
    print("   Top 5 students by GPA:")
    for i, student in enumerate(stats['top_5_students'], 1):
        print(f"     {i}. {student['fio']} - {student['gpa']}")
    
    print("\n7. Removing student 'Васильев Денис Олегович':")
    if group.remove("Васильев Денис Олегович"):
        print("   Student removed successfully")
    
    print("\n8. Exporting data to JSON:")
    json_path = "data/lab09/students_export.json"
    if group.export_to_json(json_path):
        print(f"   Data exported to {json_path}")
    
    print("\n=== Testing completed ===")