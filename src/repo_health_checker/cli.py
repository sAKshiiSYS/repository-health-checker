
from pathlib import Path

from repo_health_checker.checker import check_repository


def main():
    repo_path = input("Enter the repository path: ").strip()

    if not Path(repo_path).is_dir():
        print("Error: That folder does not exist.")
        return

    results = check_repository(repo_path)

    print("\nRepository Health Report")
    print("-" * 30)

    for filename, exists in results.items():
        status = "FOUND" if exists else "MISSING"
        print(f"{filename}: {status}")

    missing_items = [
        filename
        for filename, exists in results.items()
        if not exists
    ]

    print("-" * 30)

    if missing_items:
        print("Missing items: " + ", ".join(missing_items))
    else:
        print("Great job! All checks passed.")

    found = sum(results.values())
    total = len(results)
    score = (found / total) * 100 if total else 0

    print(f"Health score: {score:.0f}% ({found}/{total} checks passed)")


if __name__ == "__main__":
    main()

