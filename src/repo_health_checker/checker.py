
from pathlib import Path


def check_repository(repo_path):
    """Check for important files and folders in a repository."""
    repo = Path(repo_path)

    required_files = ["README.md", "LICENSE", ".gitignore"]

    results = {}

    for filename in required_files:
        results[filename] = (repo / filename).is_file()

    results["tests/"] = (repo / "tests").is_dir()

    return results
