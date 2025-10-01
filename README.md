# Test Repository

A simple Python test repository for dependency testing.

## Structure

```
test/
├── main.py              # Main script that depends on dependency.py
├── src/
│   ├── dependency.py    # Contains utility functions
│   └── random.py        # Standalone script that prints "Hello World!"
└── .gitignore          # Ignores Python cache files
```

## Files

- **main.py**: Imports and uses functions from `dependency.py` to demonstrate module dependencies
- **src/dependency.py**: Contains `greet()` and `add_numbers()` utility functions
- **src/random.py**: A simple standalone script that prints "Hello World!"

## Usage

Run the main script:
```bash
python3 main.py
```

Run the random script:
```bash
python3 src/random.py
```

## Requirements

- Python 3.x
