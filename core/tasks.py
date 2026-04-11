import datetime

def add_task(tasks: dict[int, dict], title: str, description: str | None = None) -> dict:
    task_id = len(tasks) + 1
    created_at = datetime.datetime.now()
    dict_task = {'id': task_id, 'title': title, 'description': description, 'is_completed': False, 'created_at': created_at}
    tasks[task_id] = dict_task
    return dict_task

def list_tasks(tasks: dict[int, dict]) -> list[dict]:
    return list(tasks.values())

def complete_task(tasks: dict[int, dict], task_id: int) -> dict | None:
    try:
        tasks[task_id]['is_completed'] = True
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