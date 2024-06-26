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

## Setup and Run Unit Tests

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

## Algorithms

### String matching algorithms

Knuth–Morris–Pratt Algorithm
Rabin-Karp algorithm (Double Hash)

## TODO

### Leetcode problems

#### Array or String

[E] 2446. Determine if Two Events Have Conflict
[H] 828. Count Unique Characters of All Substrings of a Given String
[M] 227. Basic Calculator II
[E] 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
[M] 3043. Find the Length of the Longest Common Prefix
[H] 3093. Longest Common Suffix Queries
[H] 214. Shortest Palindrome
[H] 459. Repeated Substring Pattern

### Two Pointers

[M] 792. Number of Matching Subsequences
[M] 1055. Shortest Way to Form String
[M] 2486. Append Characters to String to Make Subsequence
[H] 42. Trapping Rain Water
[M] 2517. Maximum Tastiness of Candy Basket
[M] 2560. House Robber IV

### Matrix

[H] 37. Sudoku Solver
[M] 54. Spiral Matrix
[M] 73. Set Matrix Zeroes
[M] 48. Rotate Image
[M] 289. Game of Life

### Intervals

[H] 352. Data Stream as Disjoint Intervals
[M] 2655. Find Maximal Uncovered Ranges
[E] 252. Meeting Rooms
[E] 495. Teemo Attacking
[H] 616. Add Bold Tag in String
[E] 605. Can Place Flowers
[M] 649. Dota2 Senate
[M] 735. Asteroid Collision

### Stack

[H] 32. Longest Valid Parentheses
[H] 301. Remove Invalid Parentheses
[M] 2116. Check if a Parentheses String Can Be Valid
[M] 839. Similar String Groups
[M] 2800. Shortest String That Contains Three Strings
[M] 2310. Sum of Numbers With Units Digit K
[M] 2240. Number of Ways to Buy Pens and Pencils
[H] 239. Sliding Window Maximum
[H] 716. Max Stack
[H] 224. Basic Calculator

### Link List

[H] 2306. Naming a Company
[H] 41. First Missing Positive
[M] 442. Find All Duplicates in an Array
[M] 1980. Find Unique Binary String
[M] 43. Multiply Strings
[M] 371. Sum of Two Integers
[M] 148. Sort List
[M] 244. Shortest Word Distance II
[M] 1634. Add Two Polynomials Represented as Linked Lists
    Note: When polynomial's coefficient == 0, the node is not added to new formular. Look out when this is happened on tail node in the new formular.
[M] 445. Add Two Numbers II
    Follow up: Could you solve it without reversing the input lists?
    Note: carry over, line up for example (1 + 99)
[M] 2807. Insert Greatest Common Divisors in Linked List
[M] 2495. Number of Subarrays Having Even Product
[E] 2843. Count Symmetric Integers
[H] 23. Merge k Sorted Lists
[M] 264. Ugly Number II
[M] 2411. Smallest Subarrays With Maximum Bitwise OR
[M] 19. Remove Nth Node From End of List
    Note: do it in one pass by using two pointer which are separated by n steps
[M] 138. Copy List With Random Pointer
    Note: First pass: clone the old node and insert the clone right after the new node
          Second pass: remove the cloned node to a new link list
    
