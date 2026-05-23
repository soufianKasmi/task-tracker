# Task Tracker CLI 📋

A simple command-line task manager built with Python. Add, update, delete, and list tasks directly from your terminal — no external libraries required.

---

## Features

- Add new tasks
- Update task status (in-progress ⚒️ or done ✅)
- Delete tasks by ID
- List all tasks with their current status
- Input validation with helpful error messages

---

## Usage

Run the program:

```bash
python task_tracker.py
```

You will see a menu:

```
1 - add task
2 - update task
3 - delete task
5 - list tasks
7 - quit
```

### Examples

**Adding a task:**
```
your choice: 1
enter the task name: Buy groceries
task id 1, added!
```

**Updating a task:**
```
your choice: 2
enter the task ID: 1
1 - in progress
2 - done
your choice: 2
task 1 updated! ✔️
```

**Listing tasks:**
```
your choice: 5
[1]  Buy groceries : done ✅
[2]  Study Python  : in progress ⚒️
```

**Deleting a task:**
```
your choice: 3
the id: 1
task 1 deleted!
```

---

## What I learned

- Python dictionaries and lists
- `input()` and menu-driven CLI design
- `try/except` for error handling
- Functions and code organization

---

## Author

Built from scratch as a beginner Python project. Inspired by [roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker).
