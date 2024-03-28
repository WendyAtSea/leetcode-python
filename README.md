# leetcode-python

Practice LeetCode problems in Python

## Setup Project and Virtual Environment

### Prerequisite

References
- https://betterstack.com/community/questions/what-are-differences-between-python-virtual-environments/
- https://realpython.com/dependency-management-python-poetry/
- https://dev.to/mattcale/pyenv-poetry-bffs-20k6

```bash
# on Mac
brew install pyenv
brew install poetry
```

### Initialize Project Environment
Use `pyenv` to manage multiple python versions
```bash
# show installed python versions
pyenv versions

# show available versions to be installed
pyenv install -l

# install python version
pyenv install 3.12.2

# uninstall python version
pyenv uninstall 3.12.0
```

Use `poetry` to manage project dependencies
```bash
# run the following commands in your project directory
pyenv local 3.12.2

# Create a poetry project
poetry init -n
cat pyproject.toml

# Initialize and start your virtual environment
poetry shell

# Add dependency
poetry add <dependency>

# Exit your virtual environment
deactivate
```

## Run Project
```bash
# start environment
poetry shell

# eixt environment
deactivate
```
