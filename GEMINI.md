# Project Overview

This directory contains a collection of Python solutions for various LeetCode problems. Each file corresponds to a single LeetCode problem and contains a Python script to solve it.

## Building and Running

There is no formal build process for this project. Individual solutions can be tested and run using the Python interpreter.

To run a specific solution, you can execute the file directly:

```bash
python3 <filename>.py
```

For files containing unit tests, you can run them as follows:

```bash
python3 test_romanToInt.py
```

## Development Conventions

*   **File Structure:** Each LeetCode problem is solved in its own Python file (e.g., `twosum.py`, `add_two_numbers.py`).
*   **Solution Class:** The solution for each problem is implemented as a method within a `Solution` class, which is a common pattern in LeetCode.
*   **Typing:** Python type hints are used to specify the types of function arguments and return values, improving code readability and maintainability.
*   **Testing:** The `unittest` framework is used for testing the solutions. Test files are named with a `test_` prefix (e.g., `test_romanToInt.py`).
