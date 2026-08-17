#!/usr/bin/env python3
"""
Simple tests for Task Manager
"""

import unittest
import os
import json
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.test_file = "test_tasks.json"
        self.tm = TaskManager(self.test_file)

    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        """Test adding a task"""
        self.tm.add_task("Buy groceries", "high")
        self.assertEqual(len(self.tm.tasks), 1)
        self.assertEqual(self.tm.tasks[0]["title"], "Buy groceries")

    def test_task_default_priority(self):
        """Test task default priority"""
        self.tm.add_task("Test task")
        self.assertEqual(self.tm.tasks[0]["priority"], "medium")

    def test_complete_task(self):
        """Test completing a task"""
        self.tm.add_task("Test task")
        self.tm.complete_task(1)
        self.assertTrue(self.tm.tasks[0]["completed"])

    def test_delete_task(self):
        """Test deleting a task"""
        self.tm.add_task("Task 1")
        self.tm.add_task("Task 2")
        self.tm.delete_task(1)
        self.assertEqual(len(self.tm.tasks), 1)

    def test_load_tasks(self):
        """Test loading tasks from file"""
        self.tm.add_task("Persistent task")
        tm2 = TaskManager(self.test_file)
        self.assertEqual(len(tm2.tasks), 1)
        self.assertEqual(tm2.tasks[0]["title"], "Persistent task")


if __name__ == "__main__":
    unittest.main()