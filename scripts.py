import json
import subprocess
import toml

from git import Repo
from pathlib import Path

settingsPath = ".vscode/settings.json"


def vscode():
    venv_path = subprocess.check_output("poetry env info --path".split())
    venv_path = venv_path.decode("UTF-8")

    settings = dict()

    Path(".vscode").mkdir(parents=True, exist_ok=True)
    Path(settingsPath).touch()

    with open(settingsPath, "r") as f:
        try:
            settings = json.load(f)
        except json.decoder.JSONDecodeError:
            pass
        settings["python.pythonPath"] = venv_path

    with open(settingsPath, "w") as f:
        json.dump(settings, f, sort_keys=True, indent=4)


def update_authors():
    filename = Path('pyproject.toml')
    config = dict()

    with open(filename, 'r') as fh:
        try:
            config = toml.load(fh)
        except toml.TomlDecodeError:
            pass
        authors = config['tool']['poetry']['authors']
        cwd = Path.cwd()
        repo = Repo(cwd)

        for commit in list(repo.iter_commits()):
            if commit.committer == commit.author:
                author = f'{commit.author.name} <{commit.author.email}>'

                if author not in authors:
                    authors.append(author)

        config['tool']['poetry']['authors'] = authors

    with open(filename, 'w') as fh:
        toml.dump(config, fh)
