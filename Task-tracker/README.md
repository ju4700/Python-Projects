# Task Tracker CLI

A simple command-line tool to manage tasks using Python and Django. This project allows users to add, update, delete, and list tasks, as well as mark tasks with different statuses (todo, in-progress, done). The task data is stored using Django models and managed via Django's Command Line Interface (CLI).

## Features

- Add tasks
- Update tasks
- Delete tasks
- List all tasks
- List tasks by status:
  - Done
  - To Do
  - In Progress
- Mark tasks as done or in progress

## Requirements

- Python 3.x
- Django

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. Set up a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply Django migrations (for database setup):

   ```bash
   python manage.py migrate
   ```

## Usage

Once the repository is set up, you can interact with the Task Tracker CLI by running the following commands from the terminal:

### Add a Task

```bash
python manage.py taskcli add "Task description"
```

### Update a Task

```bash
python manage.py taskcli update <task_id> "Updated task description"
```

### Delete a Task

```bash
python manage.py taskcli delete <task_id>
```

### Mark a Task as In Progress

```bash
python manage.py taskcli mark-in-progress <task_id>
```

### Mark a Task as Done

```bash
python manage.py taskcli mark-done <task_id>
```

### List All Tasks

```bash
python manage.py taskcli list
```

### List Tasks by Status

To list tasks by status (`todo`, `in-progress`, `done`):

```bash
python manage.py taskcli list <status>
```

**Examples:**

- List all tasks that are done:

  ```bash
  python manage.py taskcli list done
  ```

- List all tasks that are not done:

  ```bash
  python manage.py taskcli list todo
  ```

## Task Properties

Each task has the following properties:

- **id**: A unique identifier for the task
- **description**: A short description of the task
- **status**: The status of the task (`todo`, `in-progress`, `done`)
- **createdAt**: The date and time when the task was created
- **updatedAt**: The date and time when the task was last updated

These properties are stored using Django models, and the task data is managed in the database.

## Task Data Storage

Tasks are stored in the database through Django models, not in a JSON file. The `task` model handles storing the task properties and their updates.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project is built using Django's Command Line Interface (CLI) and models to store and manage tasks.
- No external libraries other than Django are used in this CLI tool.
```

### Key Updates:

- The storage is now explicitly described as using Django models and database, rather than a JSON file.
- Instructions for applying Django migrations have been added.
