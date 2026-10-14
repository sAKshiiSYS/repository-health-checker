# Contributing to Repository Health Checker

Thank you for your interest in contributing to Repository Health Checker! This project aims to help developers check the basic health of their software repositories.

## Getting Started

### 1. Set Up the Project

Make sure Python 3.10 or later and Git are installed.

Clone the repository:

```bash
git clone https://github.com/sAKshiiSYS/repository-health-checker.git
cd repository-health-checker
```

Install the project and development dependencies:

```bash
py -m pip install -e ".[dev]"
```

### 2. Find Something to Work On

- Check the open GitHub Issues for tasks.
- Choose an issue that matches your skills and experience.
- If required by the project maintainers, ask to be assigned before starting work.
- Ask questions if the requirements are unclear.

### 3. Make Your Changes

Create a separate branch for your work:

```bash
git switch -c feature/your-feature-name
```

Make focused changes related to your issue.

### 4. Run the Tests

Before submitting your changes, run:

```bash
py -m pytest
```

Make sure the tests pass.

### 5. Submit a Pull Request

Commit and push your changes:

```bash
git add .
git commit -m "Describe your changes"
git push -u origin feature/your-feature-name
```

Then open GitHub and create a pull request against the `main` branch.

In your pull request:

- Explain what you changed.
- Link the related issue, if applicable.
- Mention the tests you ran.
- Respond respectfully to review feedback.

## Contribution Guidelines

- Keep changes focused and easy to review.
- Write clear commit messages.
- Add or update tests when changing functionality.
- Do not commit virtual environments, cache files, secrets, or unnecessary generated files.
- Be respectful and welcoming to other contributors.

Thank you for helping improve Repository Health Checker!
