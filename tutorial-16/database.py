# models.py
from sqlalchemy import Column, Integer, String, create_engine, inspect, MetaData, Table, text

# ----------------------
# Database connection
# ----------------------
engine = create_engine('sqlite:///tutorial_16.sqlite', echo=True)
metadata = MetaData()

# ----------------------
# Define students table
# ----------------------
students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('roll_number', Integer),
    Column('age', Integer)
)

# Create table if it doesn't exist
def create_students_table():
    inspector = inspect(engine)
    if not inspector.has_table("students"):
        metadata.create_all(engine)

# ----------------------
# Connection helper
# ----------------------
def db_connection():
    return engine.connect()

# ----------------------
# CRUD functions
# ----------------------
def get_all_students():
    con = db_connection()
    result = con.execute(text("SELECT * FROM students")).mappings().all()
    con.close()
    return result

def get_student(student_id: int):
    con = db_connection()
    result = con.execute(
        text("SELECT * FROM students WHERE id = :id"),
        {"id": student_id}
    ).mappings().first()
    con.close()
    return result

def create_student(name: str, roll_number: int, age: int):
    con = db_connection()
    con.execute(
        text("""
        INSERT INTO students (name, roll_number, age)
        VALUES (:name, :roll, :age)
        """),
        {"name": name, "roll": roll_number, "age": age}
    )
    con.commit()
    con.close()

def update_student(student_id: int, name: str = None, roll_number: int = None, age: int = None):
    con = db_connection()
    # Build dynamic update based on which fields are provided
    query_parts = []
    params = {"id": student_id}

    if name is not None:
        query_parts.append("name = :name")
        params["name"] = name
    if roll_number is not None:
        query_parts.append("roll_number = :roll")
        params["roll"] = roll_number
    if age is not None:
        query_parts.append("age = :age")
        params["age"] = age

    if query_parts:
        query = f"UPDATE students SET {', '.join(query_parts)} WHERE id = :id"
        con.execute(text(query), params)
        con.commit()
    con.close()

def delete_student(student_id: int):
    con = db_connection()
    con.execute(text("DELETE FROM students WHERE id = :id"), {"id": student_id})
    con.commit()
    con.close()