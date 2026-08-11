"""
🐍 Day 60: Milestone Mini Project — Task Manager App
Combines everything from Day 51-59:
itertools, Context Managers, Threading, SQLite,
Unit Testing, Logging, datetime, Dataclasses, Type Hints
"""

import sqlite3
import logging
import unittest
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional
from contextlib import contextmanager

# ----------------------------------------------------
# 1. Logging setup (Day 56)
# ----------------------------------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("TaskManager")
logger.propagate = False
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(handler)


# ----------------------------------------------------
# 2. Task dataclass with type hints (Day 58 + Day 59)
# ----------------------------------------------------

@dataclass
class Task:
    id: Optional[int]
    title: str
    due_date: date
    priority: str = "Medium"
    completed: bool = False

    def days_remaining(self) -> int:
        return (self.due_date - date.today()).days

    def is_overdue(self) -> bool:
        return not self.completed and self.days_remaining() < 0


# ----------------------------------------------------
# 3. Context manager for safe DB connections (Day 52)
# ----------------------------------------------------

@contextmanager
def db_connection(db_name: str):
    conn = sqlite3.connect(db_name)
    logger.info(f"Opened connection to {db_name}")
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()
        logger.info(f"Closed connection to {db_name}")


# ----------------------------------------------------
# 4. TaskManager class -> SQLite-backed storage (Day 54)
# ----------------------------------------------------

class TaskManager:
    def __init__(self, db_name: str = "tasks.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self) -> None:
        with db_connection(self.db_name) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    due_date TEXT NOT NULL,
                    priority TEXT DEFAULT 'Medium',
                    completed INTEGER DEFAULT 0
                )
            """)

    def add_task(self, task: Task) -> None:
        with db_connection(self.db_name) as conn:
            conn.execute(
                "INSERT INTO tasks (title, due_date, priority, completed) VALUES (?, ?, ?, ?)",
                (task.title, task.due_date.isoformat(), task.priority, int(task.completed))
            )
        logger.info(f"Added task: {task.title}")

    def get_all_tasks(self) -> List[Task]:
        with db_connection(self.db_name) as conn:
            rows = conn.execute("SELECT id, title, due_date, priority, completed FROM tasks").fetchall()

        # list comprehension (Day 25) turning rows into Task objects
        return [
            Task(
                id=row[0],
                title=row[1],
                due_date=date.fromisoformat(row[2]),
                priority=row[3],
                completed=bool(row[4])
            )
            for row in rows
        ]

    def complete_task(self, task_id: int) -> None:
        with db_connection(self.db_name) as conn:
            conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        logger.info(f"Marked task #{task_id} as completed")

    def overdue_tasks(self) -> List[Task]:
        return [t for t in self.get_all_tasks() if t.is_overdue()]

    def tasks_by_priority(self, priority: str) -> List[Task]:
        return list(filter(lambda t: t.priority == priority, self.get_all_tasks()))


# ----------------------------------------------------
# 5. Using the Task Manager
# ----------------------------------------------------

manager = TaskManager("tasks.db")

manager.add_task(Task(id=None, title="Finish Python course", due_date=date.today() + timedelta(days=5), priority="High"))
manager.add_task(Task(id=None, title="Buy groceries", due_date=date.today() - timedelta(days=2), priority="Low"))
manager.add_task(Task(id=None, title="Submit report", due_date=date.today() + timedelta(days=1), priority="High"))

print("\n--- All Tasks ---")
for t in manager.get_all_tasks():
    status = "✅ Done" if t.completed else ("⚠️ Overdue" if t.is_overdue() else f"{t.days_remaining()}d left")
    print(f"[{t.id}] {t.title} ({t.priority}) - {status}")

print("\n--- Overdue Tasks ---")
for t in manager.overdue_tasks():
    print(f"{t.title} was due on {t.due_date}")

print("\n--- High Priority Tasks ---")
for t in manager.tasks_by_priority("High"):
    print(t.title)

# Complete a task
first_task = manager.get_all_tasks()[0]
manager.complete_task(first_task.id)

print("\n--- After completing a task ---")
for t in manager.get_all_tasks():
    print(f"[{t.id}] {t.title} - Completed: {t.completed}")


# ----------------------------------------------------
# 6. Unit tests for the Task dataclass logic (Day 55)
# ----------------------------------------------------

class TestTask(unittest.TestCase):
    def test_days_remaining(self):
        task = Task(id=1, title="Test", due_date=date.today() + timedelta(days=3))
        self.assertEqual(task.days_remaining(), 3)

    def test_is_overdue_true(self):
        task = Task(id=2, title="Late Task", due_date=date.today() - timedelta(days=1))
        self.assertTrue(task.is_overdue())

    def test_is_overdue_false_when_completed(self):
        task = Task(id=3, title="Done Task", due_date=date.today() - timedelta(days=1), completed=True)
        self.assertFalse(task.is_overdue())

print("\n--- Running unit tests ---")
runner = unittest.TextTestRunner(verbosity=2)
runner.run(unittest.TestLoader().loadTestsFromTestCase(TestTask))


# ----------------------------------------------------
# 7. Cleanup
# ----------------------------------------------------

import os
os.remove("tasks.db")
print("\nDemo database cleaned up.")


"""
📝 Quick Recap — Skills used in this milestone project:
- Dataclasses + type hints for a clean Task model
- Context managers for safe, auto-closing DB connections
- SQLite for persistent storage (CRUD operations)
- Logging for tracking application events
- datetime/timedelta for due dates and overdue calculations
- List comprehensions and filter() for querying tasks
- Unit tests verifying the Task's business logic
- This mirrors a real to-do/task-tracking application backend!
"""