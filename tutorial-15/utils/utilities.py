from config import secrets, config
import json

data_path = secrets.data_path

def load_students(path: str = data_path):
    with open(path, "r") as f:
        students_data = f.read()
    print(type(students_data)) 
    return json.loads(students_data)


def get_student_by_roll_number(roll_number: str, path: str = data_path):
    students = load_students(path)
    for student in students:
        if student["roll_number"] == roll_number:
            return student
    return ValueError("Student with roll number {} not found".format(roll_number))


def add_new_student(student: dict, path: str = data_path):
    students = load_students(path)
    students.append(student)
    with open(path, "w") as f:
        json.dump(students, f, indent=4)


def update_student_by_roll_number(roll_number: str, name: str, age: int, city: str, path: str = data_path):
    students = load_students(path)
    for student in students:
        if student["roll_number"] == roll_number:
            student["name"] = name
            student["age"] = age
            student["city"] = city
            with open(path, "w") as f:
                json.dump(students, f, indent=4)
            return student
    raise ValueError("Student with roll number {} not found".format(roll_number))


def delete_student_by_roll_number(roll_number: str, path: str = data_path):
    students = load_students(path)
    for i, student in enumerate(students):
        if student["roll_number"] == roll_number:
            del students[i]
            with open(path, "w") as f:
                json.dump(students, f, indent=4)
            return {"message": "Student with roll number {} deleted successfully".format(roll_number)}
    raise ValueError("Student with roll number {} not found".format(roll_number))


# if __name__ == "__main__":
#     print(load_students())
#     print(get_student("A26-102"))  
#     print(delete_student("A26-101"))
#     print(add_student({'roll_number': 'A26-101', 'name': 'Ali Khan', 'age': 20, 'city': 'Multan'}))
#     print(update_student(roll_number="A26-101", name="Ali Khan Updated", age=21, city="Karachi"))