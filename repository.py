import sqlite3
from datetime import datetime
from database import get_connection


class TaskRepository:

    def get_all(self) -> list[dict]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get_by_id(self, task_id: int) -> dict | None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def create(self, title: str, description: str | None) -> dict:
        conn = get_connection()
        cursor = conn.cursor()
        created_at = datetime.now().isoformat()
        cursor.execute(
            "INSERT INTO tasks (title, description, is_completed, created_at) VALUES (?, ?, 0, ?)",
            (title, description, created_at),
        )
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        return self.get_by_id(task_id)

    def update(self, task_id: int, title: str, description: str | None) -> dict | None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET title = ?, description = ? WHERE id = ?",
            (title, description, task_id),
        )
        conn.commit()
        conn.close()
        return self.get_by_id(task_id)

    def complete(self, task_id: int) -> dict | None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET is_completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        return self.get_by_id(task_id)

    def delete(self, task_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted
