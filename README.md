\# Todo List



Простое приложение для управления списком задач.

На текущем этапе работает как CLI (консольное приложение),

в будущем будет переписано в REST API на FastAPI.



\## Стек



\- Python 3.14

\- Стандартная библиотека (без внешних зависимостей)



\## Как запустить локально



\### Требования



\- Установленный Python 3.10+

\- Git



\### Установка



1\. Клонировать репозиторий:



```bash

&#x20;  git clone https://github.com/Artory06/ToDo-List.git

&#x20;  cd "ToDo List"

```



2\. Создать виртуальное окружение:



```bash

&#x20;  python -m venv .venv

```



3\. Активировать его:



&#x20;  - Windows (Git Bash): `source .venv/Scripts/activate`

&#x20;  - Windows (PowerShell): `.venv\\Scripts\\Activate.ps1`

&#x20;  - macOS / Linux: `source .venv/bin/activate`



4\. Установить зависимости:



```bash

&#x20;  pip install -r requirements.txt

```



\### Запуск



```bash

python main.py

```



Откроется меню в терминале:

```

1\. Добавить задачу

2\. Показать список задач

3\. Отметить задачу выполненной

4\. Удалить задачу

5\. Выход

```

\## Структура проекта

```

ToDo List/

├── main.py              # точка входа, CLI

├── core/

│   ├── \_\_init\_\_.py

│   └── tasks.py         # классы Task, TaskService, TaskNotFoundError

├── requirements.txt     # зависимости

├── .gitignore

└── README.md

```

