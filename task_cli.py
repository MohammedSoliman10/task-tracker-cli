import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task description.")
            sys.exit(1)
        description = sys.argv[2]
        tasks = load_tasks()
        new_id = len(tasks) + 1
        new_task = {
            "id": new_id,
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task added successfully (ID: {new_id})")
    elif command == "list":
        tasks = load_tasks()
        if len(sys.argv) == 2:
            filtered = tasks
        elif sys.argv[2] == "done":
            filtered = [task for task in tasks if task["status"] == "done"]
        elif sys.argv[2] == "todo":
            filtered = [task for task in tasks if task["status"] == "todo"]
        elif sys.argv[2] == "in-progress":
            filtered = [task for task in tasks if task["status"] == "in-progress"]
        else:
            print(f"Unknown filter: {sys.argv[2]}")
            sys.exit(1)

        if len(filtered) == 0:
            print("No tasks found.")
        else:
            for task in filtered:
                print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']})")
    
    elif command == "update":
        if len(sys.argv) < 4:
            print("Please provide a task ID and new description.")
            sys.exit(1)
        task_id = int(sys.argv[2])
        new_description = sys.argv[3]
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_tasks(tasks)
                print(f"Task {task_id} updated successfully.")
                sys.exit(0)
        print(f"Task with ID {task_id} not found.")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide a task ID.")
            sys.exit(1)
        task_id = int(sys.argv[2])
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print(f"Task {task_id} deleted successfully.")
                sys.exit(0)
        print(f"Task with ID {task_id} not found.")
    
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Please provide a task ID.")
            sys.exit(1)
        task_id = int(sys.argv[2])
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "in-progress"
                task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_tasks(tasks)
                print(f"Task {task_id} marked as in-progress.")
                sys.exit(0)
        print(f"Task with ID {task_id} not found.")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Please provide a task ID.")
            sys.exit(1)
        task_id = int(sys.argv[2])
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_tasks(tasks)
                print(f"Task {task_id} marked as done.")
                sys.exit(0)
        print(f"Task with ID {task_id} not found.")


    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()  