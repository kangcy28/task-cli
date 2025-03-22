# Task Tracker CLI

A simple command-line interface for tracking tasks, built with Python.

## Features

- Add, update, and delete tasks
- Mark tasks as in-progress or done
- List all tasks or filter by status
- Persistent storage in JSON format
- Simple and easy-to-use interface

## Installation

### Prerequisites

- Python 3.6 or higher

### Windows Setup

1. **Clone or download this repository**

2. **Create a batch file for easy access**

   Create a file named `task-cli.bat` with the following content:
   ```batch
   @echo off
   python "C:\path\to\task_cli.py" %*
   ```
   Replace `C:\path\to\task_cli.py` with the actual path to the script.

3. **Add to PATH (Optional)**

   - Place the batch file in a directory that's in your PATH, or
   - Add the directory containing the batch file to your PATH environment variable

### macOS/Linux Setup

1. **Clone or download this repository**

2. **Make the script executable**
   ```bash
   chmod +x task_cli.py
   ```

3. **Create a symbolic link (Optional)**
   ```bash
   sudo ln -s /full/path/to/task_cli.py /usr/local/bin/task-cli
   ```

## Usage

### Basic Commands

```
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating a task
task-cli update 1 "Buy groceries and cook dinner"
# Output: Task 1 updated successfully

# Deleting a task
task-cli delete 1
# Output: Task 1 deleted successfully

# Marking a task as in-progress
task-cli mark-in-progress 1
# Output: Task 1 marked as in-progress

# Marking a task as done
task-cli mark-done 1
# Output: Task 1 marked as done
```

### Listing Tasks

```
# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list todo
task-cli list in-progress
task-cli list done
```

## Data Storage

All tasks are stored in a JSON file named `tasks.json` in the same directory as the script. Each task contains:

- ID
- Description
- Status (todo, in-progress, done)
- Creation timestamp
- Last update timestamp

## Troubleshooting

### File Not Creating/Updating

If tasks.json isn't being created or updated:

1. **Check file location**: By default, the file is created in the current working directory
2. **Try using absolute path**: Modify `TASKS_FILE` in the script to use an absolute path
3. **Check permissions**: Ensure you have write permissions for the directory

### Command Not Found

If you get "command not found" errors:

1. **Check your PATH**: Ensure the batch file or script is in your PATH
2. **Use full path**: Call the script or batch file with its full path
3. **Verify execution permissions**: Ensure the script is executable (Linux/macOS)

## Extending the Tool

Here are some ideas for extending this tool:

- Add due dates for tasks
- Implement task priorities
- Add support for categories or tags
- Implement search functionality
- Add more detailed reporting

## License

This project is open source and available under the [MIT License](LICENSE).