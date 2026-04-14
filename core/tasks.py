import datetime

class TaskNotFoundError(Exception):
    pass



class Task:
    def __init__(self, title: str, description: str | None = None) -> None:
        self.id = 1
        self.title = title
        self.description = description
        self.is_completed = False
        self.created_at = datetime.datetime.now()

    def __str__(self) -> str:
        status = '✔' if self.is_completed else ' '
        return f"[{status}] №{self.id} {self.title}"

    def complete(self) -> None:
        self.is_completed = True

    def update_title(self, new_title: str) -> None:
        self.title = new_title


class TaskService:
    def __init__(self) -> None:
        self.tasks: dict[int, Task] = {}
        self.next_id: int = 1

    def add(self, title: str, description: str | None = None) -> Task:
        task = Task(title, description)
        task.id = self.next_id
        self.next_id += 1
        self.tasks[task.id] = task
        return task

    def list_all(self) -> list[Task]:
        return list(self.tasks.values())

    def complete(self, task_id: int) -> Task:
        task = self.tasks.get(task_id)
        if task is None:
            raise TaskNotFoundError(f'Задача {task_id} не найдена')
        task.complete()
        return task

    def delete(self, task_id: int) -> Task:
        task = self.tasks.pop(task_id, None)
        if task is None:
            raise TaskNotFoundError(f"Задача {task_id} не найдена")
        return task


def add_task(
    tasks: dict[int, dict], title: str, description: str | None = None
) -> dict:
    task_id = len(tasks) + 1
    created_at = datetime.datetime.now()
    dict_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "is_completed": False,
        "created_at": created_at,
    }
    tasks[task_id] = dict_task
    return dict_task


def list_tasks(tasks: dict[int, dict]) -> list[dict]:
    return list(tasks.values())


def complete_task(tasks: dict[int, dict], task_id: int) -> dict | None:
    try:
        tasks[task_id]["is_completed"] = True
        return tasks[task_id]
    except KeyError:
        return None


def delete_task(tasks: dict[int, dict], task_id: int) -> dict | None:
    try:
        want_to_delete = tasks[task_id]
        del tasks[task_id]
        return want_to_delete
    except KeyError:
        return None
