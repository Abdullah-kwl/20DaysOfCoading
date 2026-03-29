from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def view():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "Start Learning FastAPI!"}