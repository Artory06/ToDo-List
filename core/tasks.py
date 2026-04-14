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



