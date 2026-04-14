from core.tasks import TaskService, TaskNotFoundError


def main():
    service = TaskService()
    while True:
        print("1. Добавить задачу")
        print("2. Показать список задач")
        print("3. Отметить задачу выполненной")
        print("4. Удалить задачу")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "5":
            break
        elif choice == "1":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи (необязательно): ")
            new_task = service.add(title, description)
            print(f"Добавлена задача #{new_task.id} - {new_task.title}")

        elif choice == "2":
            all_tasks = service.list_all()
            if len(all_tasks) == 0:
                print("Задач пока нет")
            else:
                for task in all_tasks:
                    print(task)

        elif choice == "3":
            try:
                task_id = int(input("Введите номер выполненной задачи: "))
            except ValueError:
                print("Введите корректный id")
                continue
            try:
                new_complete_task = service.complete(task_id)
                print(f"Задача {new_complete_task.id} выполнена")
            except TaskNotFoundError as e:
                print(e)

        elif choice == "4":
            try:
                task_id = int(input("Введите номер удаляемой задачи: "))
            except ValueError:
                print("Введите корректный id")
                continue
            try:
                new_delete_task = service.delete(task_id)
                print(f"Задача {new_delete_task.id} удалена")
            except TaskNotFoundError as e:
                print(e)

        else:
            print("Такого действия нет")


if __name__ == "__main__":
    main()
