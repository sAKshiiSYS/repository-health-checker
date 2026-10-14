
from repo_health_checker.cli import main


def test_main_lists_missing_items(monkeypatch, tmp_path, capsys):
    (tmp_path / "README.md").touch()
    (tmp_path / ".gitignore").touch()
    (tmp_path / "src").mkdir()
    (tmp_path / "tests").mkdir()

    monkeypatch.setattr("builtins.input", lambda _: str(tmp_path))

    main()

    output = capsys.readouterr().out

    assert "Missing items:" in output
    assert "LICENSE" in output
    assert "Health score:" in output


def test_main_shows_success_when_all_checks_pass(
    monkeypatch, tmp_path, capsys
):
    (tmp_path / "README.md").touch()
    (tmp_path / "LICENSE").touch()
    (tmp_path / ".gitignore").touch()
    (tmp_path / "src").mkdir()
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_example.py").touch()

    monkeypatch.setattr("builtins.input", lambda _: str(tmp_path))

    main()

    output = capsys.readouterr().out

    assert "Great job! All checks passed." in output
    assert "Health score: 100%" in output
