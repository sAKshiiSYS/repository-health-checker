
from pathlib import Path


def check_repository(repo_path):
    """Check for important files and folders in a repository."""
    repo = Path(repo_path)

    required_files = ["README.md", "LICENSE", ".gitignore"]

    results = {}

    for filename in required_files:
        results[filename] = (repo / filename).is_file()

    results["src/"] = (repo / "src").is_dir()

    tests_dir = repo / "tests"
    results["tests/"] = (
        tests_dir.is_dir()
        and any(tests_dir.iterdir())
    )

    return results
