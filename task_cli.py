#!/usr/bin/env python3
import sys
import json
import os
from datetime import datetime

# File to store the tasks
TASKS_FILE = "tasks.json"

# Task statuses
TODO = "todo"
IN_PROGRESS = "in-progress"
DONE = "done"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        # 在 load_tasks 函數中添加這行
        print(f"Tasks file location: {os.path.abspath(TASKS_FILE)}")
        with open(TASKS_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"tasks": [], "next_id": 1}
    return {"tasks": [], "next_id": 1}

def save_tasks(data):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Tasks saved to: {os.path.abspath(TASKS_FILE)}")
    # 驗證文件是否存在
    if os.path.exists(TASKS_FILE):
        print(f"Verified: File exists with size {os.path.getsize(TASKS_FILE)} bytes")
    else:
        print("Warning: File was not created!")

def add_task(description):
    """Add a new task with the given description."""
    data = load_tasks()
    task_id = data["next_id"]
    
    task = {
        "id": task_id,
        "description": description,
        "status": TODO,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    data["tasks"].append(task)
    data["next_id"] += 1
    save_tasks(data)
    
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, description):
    """Update the description of a task with the given ID."""
    data = load_tasks()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["description"] = description
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(data)
            print(f"Task {task_id} updated successfully")
            return
    
    print(f"Error: Task with ID {task_id} not found")

def delete_task(task_id):
    """Delete a task with the given ID."""
    data = load_tasks()
    initial_length = len(data["tasks"])
    data["tasks"] = [task for task in data["tasks"] if task["id"] != task_id]
    
    if len(data["tasks"]) < initial_length:
        save_tasks(data)
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Error: Task with ID {task_id} not found")

def mark_task_status(task_id, status):
    """Mark a task with the given status."""
    data = load_tasks()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(data)
            print(f"Task {task_id} marked as {status}")
            return
    
    print(f"Error: Task with ID {task_id} not found")

def list_tasks(status=None):
    """List all tasks or tasks with the specified status."""
    data = load_tasks()
    
    if not data["tasks"]:
        print("No tasks found")
        return
    
    filtered_tasks = data["tasks"]
    if status:
        filtered_tasks = [task for task in data["tasks"] if task["status"] == status]
    
    if not filtered_tasks:
        print(f"No tasks with status '{status}' found")
        return
    
    print("\nID | Status      | Description")
    print("-" * 50)
    
    for task in filtered_tasks:
        print(f"{task['id']:<3}| {task['status']:<12}| {task['description']}")

def print_usage():
    """Print usage instructions."""
    print("\nUsage:")
    print("  task-cli add \"<description>\"")
    print("  task-cli update <id> \"<description>\"")
    print("  task-cli delete <id>")
    print("  task-cli mark-in-progress <id>")
    print("  task-cli mark-done <id>")
    print("  task-cli list")
    print("  task-cli list [todo|in-progress|done]")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return
    
    command = sys.argv[1]
    
    if command == "add" and len(sys.argv) == 3:
        add_task(sys.argv[2])
    
    elif command == "update" and len(sys.argv) == 4:
        try:
            task_id = int(sys.argv[2])
            update_task(task_id, sys.argv[3])
        except ValueError:
            print("Error: Task ID must be a number")
    
    elif command == "delete" and len(sys.argv) == 3:
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number")
    
    elif command == "mark-in-progress" and len(sys.argv) == 3:
        try:
            task_id = int(sys.argv[2])
            mark_task_status(task_id, IN_PROGRESS)
        except ValueError:
            print("Error: Task ID must be a number")
    
    elif command == "mark-done" and len(sys.argv) == 3:
        try:
            task_id = int(sys.argv[2])
            mark_task_status(task_id, DONE)
        except ValueError:
            print("Error: Task ID must be a number")
    
    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        elif len(sys.argv) == 3 and sys.argv[2] in [TODO, IN_PROGRESS, DONE]:
            list_tasks(sys.argv[2])
        else:
            print(f"Error: Invalid status. Use {TODO}, {IN_PROGRESS}, or {DONE}")
    
    else:
        print_usage()

if __name__ == "__main__":
    main()  