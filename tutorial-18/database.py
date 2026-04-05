from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session, select

# ----------------------
# Single model for ORM + validation
# ----------------------
class StudentModel(SQLModel, table=True):
    roll_number: int = Field(primary_key=True, unique=True, index=True)  # primary key
    name: str
    age: int

    @property
    def is_adult(self) -> bool:
        return self.age >= 18

# ----------------------
# Engine
# ----------------------
engine = create_engine("sqlite:///tutorial_18.sqlite", echo=True)

# ----------------------
# Table creation
# ----------------------
def create_students_table():
    SQLModel.metadata.create_all(engine)

# ----------------------
# Dependency
# ----------------------
def get_db():
    with Session(engine) as session:
        yield session

# ----------------------
# CRUD functions
# ----------------------
def get_all_students(session: Session):
    return session.exec(select(StudentModel)).all()

def get_student(session: Session, roll_number: int):
    return session.get(StudentModel, roll_number)

def create_student(session: Session, student: StudentModel):
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

def update_student(session: Session, roll_number: int, student_data: StudentModel):
    student = session.get(StudentModel, roll_number)
    if not student:
        return None
    student.name = student_data.name
    student.age = student_data.age
    session.commit()
    session.refresh(student)
    return student

def delete_student(session: Session, roll_number: int):
    student = session.get(StudentModel, roll_number)
    if student:
        session.delete(student)
        session.commit()
    return student