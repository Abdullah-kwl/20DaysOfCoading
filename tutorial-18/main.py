from sqlmodel import Session
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from database import (StudentModel, get_db, create_student, get_all_students, 
                      get_student, update_student, delete_student, create_students_table)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_students_table()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/students/", response_model=list[StudentModel])
def read_students(db: Session = Depends(get_db)):
    return get_all_students(db)

@app.post("/students/", response_model=StudentModel)
def add_student(student: StudentModel, db: Session = Depends(get_db)):
    if not student.is_adult:
        raise HTTPException(status_code=400, detail="Student must be adult")
    return create_student(db, student)

@app.get("/students/{roll_number}", response_model=StudentModel)
def read_student(roll_number: int, db: Session = Depends(get_db)):
    student = get_student(db, roll_number)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.patch("/students/{roll_number}", response_model=StudentModel)
def patch_student(roll_number: int, student: StudentModel, db: Session = Depends(get_db)):
    if not student.is_adult:
        raise HTTPException(status_code=400, detail="Student must be adult")
    updated = update_student(db, roll_number, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@app.delete("/students/{roll_number}")
def remove_student(roll_number: int, db: Session = Depends(get_db)):
    deleted = delete_student(db, roll_number)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}