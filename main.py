from core.tasks import add_task, delete_task, complete_task, list_tasks

def main():
    tasks = {}
    while True:
        print('1. Добавить задачу')
        print('2. Показать список задач')
        print('3. Отметить задачу выполненной')
        print('4. Удалить задачу')
        print('5. Выход')
        choice = input('Выберите действие: ')

        if choice == '5':
            break
        elif choice == '1':
            title = input('Введите название задачи: ')
            description = input('Введите описание задачи (необязательно): ')
            new_task = add_task(tasks, title, description)
            print(f"Добавлена задача #{new_task['id']} - {new_task['title']}")

        elif choice == '2':
            all_tasks = list_tasks(tasks)
            if len(all_tasks) == 0:
                print('Задач пока нет')
            else:
                for task in all_tasks:
                    status = '✔' if task['is_completed'] else ' '
                    print(f"{status} №{task['id']}: {task['title']}")
        
        elif choice == '3':
            try:
                task_id = int(input('Введите номер выполненной задачи: '))
            except ValueError:
                print('Введите корректный id')
                continue
            new_complete_task = complete_task(tasks, task_id)
            if new_complete_task is None:
                print('Задача не найдена')
            else:
                print(f"✔ Задача {new_complete_task['id']} - выполнена!")
            
        elif choice == '4':
            try:
                task_id = int(input('Введите номер удаляемой задачи: '))
            except ValueError:
                print('Введите корректный id')
                continue
            new_delete_task = delete_task(tasks, task_id)
            if new_delete_task is None:
                print('Задача не найдена')
            else:
                print(f"Задача {new_delete_task['id']} - удалена!")

        else:
            print('Такого действия нет')

if __name__ == "__main__": 
    main()