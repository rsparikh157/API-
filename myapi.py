from fastapi import FastAPI
#thus we imported FastAPI as object.
#Now we'll create an instance of this object

app = FastAPI()

students = {
    1: {
        "name" : "rutv",
        "age" : 19,
        "class" : "second year"
    }

}


@app.get("/")
def index():
    return {"name" : "First entry"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]
