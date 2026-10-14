
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

    found = sum(results.values())
    total = len(results)
    score = (found / total) * 100 if total else 0

    print("-" * 30)
    print(f"Health score: {score:.0f}% ({found}/{total} checks passed)")


if __name__ == "__main__":
    main()
