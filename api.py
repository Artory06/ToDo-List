from fastapi import FastAPI, HTTPException
from core.tasks import TaskService, TaskNotFoundError
from schemas import TaskCreate, TaskResponse

app = FastAPI()
service = TaskService()


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return service.list_all()


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    try:
        return service.get(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Задача {task_id} не найдена")


@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task_data: TaskCreate):
    return service.add(task_data.title, task_data.description)


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskCreate):
    try:
        return service.update(task_id, task_data.title, task_data.description)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Задача {task_id} не найдена")


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    try:
        service.delete(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Задача {task_id} не найдена")
