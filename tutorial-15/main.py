from typing import Optional
from fastapi import FastAPI, Path, Query, Body
from models.schemas import Student, StudentUpdate
from utils.enums import SortField, Section, SortOrder
from utils.utilities import (load_students, get_student_by_roll_number,
                             add_new_student, update_student_by_roll_number,
                             delete_student_by_roll_number)



app = FastAPI()

@app.get("/students")
def get_all_students(
    sort_by: Optional[SortField] = Query(default=None, description="Sort by 'age' or 'name'"),
    order: SortOrder = Query(default=SortOrder.asc, description="Sorting order: 'asc' or 'desc'"),
    section: Optional[Section] = Query(default=None, description="Filter by section: A, B, C")
):
    students = load_students()
    # Filter by section
    if section:
        section_str = section.value.upper()
        students = [
            s for s in students
            if s.get("roll_number", "").startswith(section_str)
        ]
    # Sorting
    if sort_by:
        students = sorted(
            students,
            key=lambda x: x.get(sort_by.value),
            reverse=True if order.value == "desc" else False
        )
    return students



@app.get("/students/{roll_number}")
def get_student(roll_number: str = Path(..., description="Get student by roll number", examples="A26-000")):
    data = get_student_by_roll_number(roll_number)
    if not data:
        return {"error": "Student not found"}
    return data


@app.post("/students")
def add_student(new_student: Student):
    try:
        student_dict = new_student.model_dump(exclude={"is_adult", "roll_numeric_part"})
        add_new_student(student=student_dict)
        return {"message": "Student added successfully"}
    except Exception as e:
        return {"error": f"Failed to add student: {str(e)}"}
    

@app.put("/students/{roll_number}")
def update_student(
    roll_number: str = Path(..., description="Update student by roll number", examples="A26-000"),
    student_data: Student = Body(..., description="Full student data to update")
):
    #Check if student exists
    existing_student = get_student_by_roll_number(roll_number)
    if not existing_student:
        return {"error": "Student not found"}
    #Convert Student model to dict, exclude computed fields
    updated_fields = student_data.model_dump(exclude={"is_adult", "roll_numeric_part"})
    #Update student in storage
    try:
        update_student_by_roll_number(roll_number, updated_fields)
        return {"message": "Student data updated successfully"}
    except ValueError as e:
        return {"error": f"Failed to update student: {str(e)}"}
    

@app.patch("/students/{roll_number}")
def patch_student(
    roll_number: str = Path(..., description="Partial update student by roll number", examples="A26-000"),
    student_data: StudentUpdate = Body(..., description="Partial student data to update")
):
    #Check if student exists
    existing_student = get_student_by_roll_number(roll_number)
    if not existing_student:
        return {"error": "Student not found"}
    #Convert StudentUpdate to dict, exclude unset fields and computed fields
    updated_fields = student_data.model_dump(exclude_unset=True, exclude={"is_adult", "roll_numeric_part"})
    if not updated_fields:
        return {"error": "No fields provided to update"}
    #Update only the provided fields
    try:
        update_student_by_roll_number(roll_number, updated_fields)
        return {"message": "Student data updated successfully"}
    except ValueError as e:
        return {"error": f"Failed to update student: {str(e)}"}
    
@app.delete("/students/{roll_number}")
def delete_student(roll_number: str = Path(..., description="Delete student by roll number", examples="A26-000")):
    try:
        delete_student_by_roll_number(roll_number)
        return {"message": "Student deleted successfully"}
    except ValueError as e:
        return {"error": f"Failed to delete student: {str(e)}"}