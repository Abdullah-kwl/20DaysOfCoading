from fastapi import FastAPI, HTTPException, Depends
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from database import (create_students_table, get_all_students, get_student, 
                      create_student, update_student, delete_student, get_db)
from schemas import StudentSchema

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_students_table()
    yield

app = FastAPI(lifespan=lifespan)

# ----------------------
# GET all students
# ----------------------
@app.get("/students/", response_model=list[StudentSchema])
def read_students(db: Session = Depends(get_db)):
    students = get_all_students(db)
    return [{"name": s.name, "roll_number": s.roll_number, "age": s.age} for s in students]

# ----------------------
# GET single student
# ----------------------
@app.get("/students/{student_id}", response_model=StudentSchema)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"name": student.name, "roll_number": student.roll_number, "age": student.age}

# ----------------------
# CREATE student
# ----------------------
@app.post("/students/")
def add_student(student: StudentSchema, db: Session = Depends(get_db)):
    if not student.is_adult:
        raise HTTPException(status_code=400, detail="Student must be adult")
    create_student(db, student.name, student.roll_number, student.age)
    return {"message": "Student added successfully"}

# ----------------------
# UPDATE student
# ----------------------
@app.patch("/students/{student_id}")
def patch_student(student_id: int, student: StudentSchema, db: Session = Depends(get_db)):
    updated = update_student(db, student_id, student.name, student.roll_number, student.age)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student updated successfully"}

# ----------------------
# DELETE student
# ----------------------
@app.delete("/students/{student_id}")
def remove_student(student_id: int, db: Session = Depends(get_db)):
    deleted = delete_student(db, student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}