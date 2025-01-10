# Python Algorithms and Data Structures

This project is a learning resource for algorithms, data structures, and their time/space complexity analysis. Each implementation includes tests and complexity analysis.

## Project Structure

```
python-algorithms/
├── src/              # Source code directory
├── requirements.txt  # Project dependencies
└── README.md        # This file
```

## Setup Instructions

1. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Tests in a Specific Directory

```bash
pytest src/sum_of_two_numbers/
```

### Watch Mode for Tests

To automatically run tests when files change:

```bash
# Watch all tests
 ptw

# Watch specific directory
 ptw  src/sum_of_two_numbers/
```

## Code Style

This project uses Ruff for code formatting and linting:

```bash
# Format code
ruff format .

# Run linter
ruff check .

# Fix auto-fixable issues
ruff check --fix .
```

## Watch Mode

This project includes a watch mode that automatically runs a file whenever it changes. This is useful during development for quick feedback loops.

To use watch mode:

```bash
make watch FILE=path/to/your/file.py
```

For example:

```bash
make watch FILE=sum_of_two_numbers.py
```

The watcher will monitor the specified file and re-run it automatically whenever changes are saved. Press Ctrl+C to stop watching.

## Quick Run Hotkey

You can quickly run the current Python file by pressing `Control + J`.

## Project Organization

- Each algorithm and data structure will be implemented in its own file
- Every implementation will include:
  - Docstrings with time/space complexity analysis
  - Example usage
  - Comments explaining the logic
