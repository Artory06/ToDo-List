import datetime

def add_task(tasks: dict[int, dict], title: str, description: str | None = None) -> dict:
    task_id = len(tasks) + 1

    created_at = datetime.datetime.now()

    dict_task = {'id': task_id, 'title': title, 'description': description, 'is_completed': False, 'created_at': created_at}

    tasks[task_id] = dict_task

    return dict_task
