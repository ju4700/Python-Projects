# GitHub Activity CLI

A simple **Command Line Interface (CLI)** tool to fetch and display the recent activity of a GitHub user. This project is built to demonstrate working with **APIs**, handling **JSON data**, and building CLI applications in Python.

---

## Features

- Fetch recent activity for any GitHub user using the **GitHub API**.
- **Filter by Event Type**: Display only specific types of events (e.g., `PushEvent`).
- **Caching**: Locally cache results to avoid repeated API requests and improve performance.
- **Enhanced Output**:
  - Text-based summary (default).
  - JSON format.
  - Tabular format (optional, requires `tabulate` library).

---

## Prerequisites

- Python 3.6 or later installed on your system.
- Internet access to fetch data from the GitHub API.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/github-activity-cli.git
   cd github-activity-cli
   ```

2. Install dependencies (optional, for tabular output):
   ```bash
   pip install tabulate
   ```

---

## Usage

Run the script using the following command:
```bash
python py_git_act.py <username> [--event-type EVENT_TYPE] [--output-format FORMAT]
```

### **Examples**

1. Fetch recent activity for a user (default text output):
   ```bash
   python py_git_act.py ju4700
   ```

2. Filter by event type (e.g., `PushEvent`):
   ```bash
   python py_git_act.py ju4700 --event-type PushEvent
   ```

3. Display output in JSON format:
   ```bash
   python py_git_act.py ju4700 --output-format json
   ```

4. Display output in tabular format:
   ```bash
   python py_git_act.py ju4700 --output-format table
   ```

---

## Output Formats

### **Default Text Format**
```plaintext
Recent Activity Summary:
- Created a new repository in ju4700/Fully-Stacked
- Created a new branch in ju4700/Fully-Stacked
- Pushed commits to ju4700/Python-Projects (13 times)
```

### **JSON Format**
```json
{
    "Created a new repository in ju4700/Fully-Stacked": 1,
    "Created a new branch in ju4700/Fully-Stacked": 1,
    "Pushed commits to ju4700/Python-Projects": 13
}
```

### **Tabular Format**
```plaintext
Activity                                      Count
------------------------------------------  -------
Created a new repository in ju4700/Fully-Stacked     1
Created a new branch in ju4700/Fully-Stacked         1
Pushed commits to ju4700/Python-Projects           13
```

---

## Caching

- Results are cached locally in the `./cache/` directory.
- Cache files are valid for 1 hour. After that, fresh data will be fetched from the GitHub API.

---

## Supported Event Types

- `PushEvent`: Commits pushed to repositories.
- `CreateEvent`: Repositories, branches, or tags created.
- `IssuesEvent`: Issues opened or closed.
- `WatchEvent`: Repositories starred.
- **...and more**, as available in the [GitHub API](https://docs.github.com/en/rest/activity/events).

---

## Project Structure

```
github-activity-cli/
├── py_git_act.py   # Main script
├── cache/          # Directory to store cached API responses
├── README.md       # Project documentation
└── requirements.txt # Optional dependencies (e.g., tabulate)
```

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or improvements.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your fork and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Tabulate Library](https://pypi.org/project/tabulate/) (for tabular output)

Enjoy using the GitHub Activity CLI! 🚀
