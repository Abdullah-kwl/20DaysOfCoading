from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from database import (create_students_table, get_all_students, 
                    get_student, create_student, update_student, 
                    delete_student)
from schemas import StudentSchema

# Run table creation at startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run once at startup
    create_students_table()
    yield
    # Optional shutdown code here

app = FastAPI(lifespan=lifespan)


# ----------------------
# GET all students
# ----------------------
@app.get("/students/", response_model=list[StudentSchema])
def read_students():
    students = get_all_students()
    return [{"name": s["name"], "roll_number": s["roll_number"], "age": s["age"]} for s in students]

# ----------------------
# GET single student
# ----------------------
@app.get("/students/{student_id}", response_model=StudentSchema)
def read_student(student_id: int):
    student = get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"name": student["name"], "roll_number": student["roll_number"], "age": student["age"]}

# ----------------------
# CREATE student
# ----------------------
@app.post("/students/")
def add_student(student: StudentSchema):
    if not student.is_adult:
        raise HTTPException(status_code=400, detail="Student must be adult")
    create_student(student.name, student.roll_number, student.age)
    return {"message": "Student added successfully"}

# ----------------------
# UPDATE student (PATCH)
# ----------------------
@app.patch("/students/{student_id}")
def patch_student(student_id: int, student: StudentSchema):
    update_student(student_id, name=student.name, roll_number=student.roll_number, age=student.age)
    return {"message": "Student updated successfully"}

# ----------------------
# DELETE student
# ----------------------
@app.delete("/students/{student_id}")
def remove_student(student_id: int):
    delete_student(student_id)
    return {"message": "Student deleted successfully"}