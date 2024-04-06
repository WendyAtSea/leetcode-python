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

# Initialize and start your virtual environment
# If you’d like to prevent poetry shell from modifying your shell prompt on virtual environment activation,
# you should set VIRTUAL_ENV_DISABLE_PROMPT=1 as an environment variable before running the command.
export VIRTUAL_ENV_DISABLE_PROMPT=1
poetry shell

# Add dependency
poetry add <dependency>

# Install dependencies
poetry install

# Exit your virtual environment
deactivate
```

## Run Project
```bash
# start environment
export VIRTUAL_ENV_DISABLE_PROMPT=1
poetry shell

# Install dependencies
poetry install

# Install without test and docs
poetry install --without test,docs

# Update dependencies
poetry update

# eixt environment
deactivate
```

## Setup Project Development Environment

https://python-poetry.org/docs/managing-dependencies/#adding-a-dependency-to-a-group

```bash
# Add test dependencies
poetry add pytest --group test
```

## Run test
```bash
# Run all the tests under "tests" directory
pytest tests -vv

# run a specific test file
pytest tests/test_medium.py -v
```
