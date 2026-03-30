from fastapi import FastAPI
from schemas import Student

app = FastAPI()

@app.get("/")
def view():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "Start Learning FastAPI!"}

@app.post("/students")
def create_student(student: Student):
    return student