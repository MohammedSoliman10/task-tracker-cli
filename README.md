# Task Tracker CLI

A simple command line app to track your tasks, built with Python.

## How to use

### Add a task
python task_cli.py add "Your task here"

### List all tasks
python task_cli.py list

### List by status
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done

### Update a task
python task_cli.py update <id> "New description"

### Delete a task
python task_cli.py delete <id>

### Mark status
python task_cli.py mark-in-progress <id>
python task_cli.py mark-done <id>