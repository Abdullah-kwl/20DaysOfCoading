from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from contextlib import contextmanager

# ----------------------
# Database connection
# ----------------------
engine = create_engine('sqlite:///tutorial_17.sqlite', echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# ----------------------
# ORM Model
# ----------------------
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    roll_number = Column(Integer)
    age = Column(Integer)

# ----------------------
# Table creation
# ----------------------
def create_students_table():
    Base.metadata.create_all(engine)

# ----------------------
# Dependency for FastAPI
# ----------------------
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------
# CRUD functions (now accept session)
# ----------------------
def get_all_students(session: Session):
    return session.query(Student).all()

def get_student(session: Session, student_id: int):
    return session.query(Student).filter_by(id=student_id).first()

def create_student(session: Session, name: str, roll_number: int, age: int):
    new_student = Student(name=name, roll_number=roll_number, age=age)
    session.add(new_student)
    session.commit()
    session.refresh(new_student)  # optional: get updated instance with id
    return new_student

def update_student(session: Session, student_id: int, name: str = None, roll_number: int = None, age: int = None):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        if name is not None:
            student.name = name
        if roll_number is not None:
            student.roll_number = roll_number
        if age is not None:
            student.age = age
        session.commit()
    return student

def delete_student(session: Session, student_id: int):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
    return student