from fastapi import FastAPI, HTTPException
from database import init_db
from repository import TaskRepository
from schemas import TaskCreate, TaskResponse

app = FastAPI()
repo = TaskRepository()


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return repo.get_all()


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = repo.get_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Задача {task_id} не найдена")
    return task


@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task_data: TaskCreate):
    return repo.create(task_data.title, task_data.description)


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskCreate):
    task = repo.update(task_id, task_data.title, task_data.description)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Задача {task_id} не найдена")
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    deleted = repo.delete(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Задача {task_id} не найдена")
