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

## Project Organization

- Each algorithm and data structure will be implemented in its own file
- Every implementation will include:
  - Docstrings with time/space complexity analysis
  - Example usage
  - Comments explaining the logic
