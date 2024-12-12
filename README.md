# GitHooks
1. Убедитесь, что у вас установлены pre-commit, flake8, isort, black (Не стал работать через venv, скачал глобально, на арче с этим отдельная заморочка, он не позволяет глобально ставить pip-пакеты, предлагает качать через pacman. Можно, конечно, создать venv, но пока не вижу смысла).
2. Установите pre-commit hook (это добавит проверки на соотвествие codestyle перед коммитом):
```bash
pre-commit install

```
3. Можно запустить проверку вручную:
```bash
pre-commit run --all-files
```
