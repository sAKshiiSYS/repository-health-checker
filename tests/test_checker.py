
from repo_health_checker.checker import check_repository


def test_check_repository_finds_existing_files(tmp_path):
    (tmp_path / "README.md").touch()
    (tmp_path / ".gitignore").touch()
    (tmp_path / "tests").mkdir()

    results = check_repository(tmp_path)

    assert results["README.md"] is True
    assert results["LICENSE"] is False
    assert results[".gitignore"] is True
    assert results["tests/"] is True
