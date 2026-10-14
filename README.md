# Repository Health Checker

A beginner-friendly Python tool that checks the basic health of a software repository.

## Features

- Checks whether `README.md` exists.
- Checks whether `LICENSE` exists.
- Checks whether `.gitignore` exists.
- Checks whether a `tests/` directory exists.
- Displays a repository health score based on the checks passed.

## Requirements

- Python 3.10 or later
- Git (for cloning the repository)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sAKshiiSYS/repository-health-checker.git
cd repository-health-checker
```

### 2. Install the project

```bash
py -m pip install -e ".[dev]"
```

### 3. Run the checker

```bash
py -c "from repo_health_checker.cli import main; main()"
```

When prompted, enter the path to the repository you want to check.

### 4. Run the tests

```bash
py -m pytest
```

## Project Structure

```text
repository-health-checker/
├── src/
│   └── repo_health_checker/
│       ├── __init__.py
│       ├── cli.py
│       └── checker.py
├── tests/
│   └── test_checker.py
├── CONTRIBUTING.md
├── pyproject.toml
└── README.md
```

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before making changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
